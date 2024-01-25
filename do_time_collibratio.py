def do_time_collibration(min, max):
    import doocs_address as addr
    import time
    import numpy as np
    import pydoocs
    #from datetime import date
    from datetime import datetime
    #print(addr.TDSphase)
    fontSize        = 14;
    num_actuator=6;
    num_bgr=10;
    num_actuator=5;
    delay = pydoocs.read(addr.camara 'TRIGGERDELAYABS')['data'];
    #pixelformat=doocswrite(addr.camara 'FORMAT.OUT')['data']; #until IAS is used:...
# set pixelformat out to mono8
    name_actuator           = 'XTDS phase';
    addr_actuator_set       = 'FLASH.RF/LLRF.CONTROLLER/CTRL.POLARIX/SP.PHASE';
    addr_actuator_rbv       = 'FLASH.RF/LLRF.CONTROLLER/FORW.SLED.POLARIX/PHASE.SAMPLE';
    timespam = datetime.now()
    timespam = datetime.now()
    date_time = timespam.strftime("%m%d%Y%H%M%S")
    filename=(date_time+'.hdf5')
    # PolariX
    frequency_XTDS          = 11.9888e9; % in Hz
    #ddd_read                = doocsread('FLASH.RF/LLRF.CONTROLLER/CTRL.POLARIX/SP.AMPL');
    #amplitude_XTDS          = ddd_read.data; % in %
    #addr_xtds_onoff         = 'FLASH.DIAG/TIMINGINFO/FLFXTDS/ON_BEAM'
    ## prepare camera
# switch off ROIs -----------------------------------------------------------
    ddd_write = pydoocs.write((addr.camara+'ROI_SPECTRUM.ON'), 0);
    ddd_write = pydoocs.write((addr.camara+'ROI2_SPECTRUM.ON'), 0);
# switch off: BG subtraction -----------------------------------------------------------
    ddd_write = pydoocs.write((addr.camara+'SUBSTR.ON'), 0);
# switch on spectrum
    ddd_write = pydoocs.write((addr.camara+'SPECTRUM.ON'), 1);

## prepare data structure -----------------------------------------------------------
    ddd_read        = pydoocs.read(addr.camara+'IMAGE_EXT');
    cam_spec        = ddd_read[data];

    # background (shot, spectrum) -----------------------------------------------------------
    bgr_x           = zeros(num_bgr, np.shape(cam_spec.val_val)[1]);
    bgr_y           = zeros(num_bgr, np.shape(cam_spec.val_val)[0]);

# signal (scan_point, shot, spectrum) -----------------------------------------------------------
    raw_spec_x      = np.zeros(num_actuator, num_sig, np.shape(cam_spec.val_val)[1]);
    corr_spec_x     = raw_spec_x;
    raw_spec_y      = np.zeros(num_actuator, num_sig, np.shape(cam_spec.val_val)[0]);
    corr_spec_y     = raw_spec_y;

    # center of mass
    pos_CoM_x       = np.zeros((num_actuator, num_sig));
    pos_CoM_y       = np.zeros((num_actuator, num_sig));

# scales
    scale_x         = np.abs(cam_spec.scale_x);
    scale_y         = np.abs(cam_spec.scale_y);
    if scale_x == 1
        scale_x         = 0.006184; # mm/pixel

        if scale_y == 1
            scale_y         = 0.006352; # mm/pixel


# current rbv -----------------------------------------------------------
    actuator_rbv    = np.zeros([1, num_actuator]);

# charge -----------------------------------------------------------
    charge_7FLFMAFF = np.zeros((num_actuator, num_sig));
    charge_7FLFDUMP = np.zeros((num_actuator, num_sig));

## prepare block laser for FLASH2 -----------------------------------------------------------

# which laser
    name_laser          = pydoocs.read('FLASH.DIAG/TIMER/FLASHCPUTIME1.0/LASER_SELECT.2')['data'];
    addr_laser_block    = 'FLASH.DIAG/BEAMLINES/FLASH/BLOCK_LASER.FLASH2';
# rep rate
    rep_rate_macro      = pydoocs.read('TTF2.UTIL/MAIN_PARAMETER/MACRO.REPRATE/VALUE')['data'];
    bits_event7         = pydoocs.read('FLASH.DIAG/TIMER/FLASHCPUTIME1.0/EVENT7')['data']; # FLASH2/FLASH3 '116'
    dividerA_event7     = bits_event7[3];
    rep_rate            = rep_rate_macro/(dividerA_event7+1);


    ## prepare actuator scan list -----------------------------------------------------------
# reference setpoint
    ref_actuator_set    = 1e-3*np.round(1e3*pydoocs.read(addr_actuator_set)['data'] );
    ref_actuator_rbv    = 1e-3*np.round(1e3*pydoocs.read(addr_actuator_rbv)['data'] );

# scan list
    scan_list_set       = np.linspace(start_actuator, end_actuator, num_actuator);
# rbv container
    scan_list_rbv       = np.zeros(num_actuator, num_sig);

    ## take background

    ddd_write = pydoocs.write([addr_cam+'TRIGGERDELAYABS'], 1000);
    print(' - changed camera delay');
    pause(2)
###################### Should be fixed -----------------------------------------------------------
# take bgr
    for jj in range(num_bgr):

    # read x
        ddd_read            = pydoocs.read(addr_cam+'SPECTRUM.X.TD');
        bgr_x[jj, :]        = ddd_read['data'];
        datatimestamp[jj]   = ddd_read['timestamp'];
        print(jj)
    ## compared it with last measurement -----------------------------------------------------------
        if jj > 1:
            while datatimestamp[jj] == datatimestamp[jj-1]:
                ddd_read        = pydoocs.read(addr_cam+'SPECTRUM.X.TD');
                bgr_x(jj,:)     = ddd_read['data'];

                print( [' same data ... wait ...']);
                time.sleep(1/rep_rate)
        ddd_read            = pydoocs.read(addr_cam+'SPECTRUM.Y.TD');
        bgr_y[jj, :]        = ddd_read['data'];
        datatimestamp[jj]   = ddd_read['timestamp'];

        if jj > 1:
            while datatimestamp[jj] == datatimestamp[jj-1]:
                ddd_read        = pydoocs.read([addr_cam+'SPECTRUM.Y.TD']);
                bgr_x(jj,:)     = ddd_read['d_gspect_array_val'];
                datatimestamp[jj]   = ddd_read['timestamp'];
                time.sleep(1/rep_rate)


    # compute mean()
    bgr_spec_x_mean = np.mean(bgr_x);
    bgr_spec_y_mean = np.mean(bgr_y);
    # take one img
    ddd_read        = doocsread([addr_cam, 'IMAGE_EXT']);
    bgr_img         = ddd_read['val_val'];

    ## scan loop -----------------------------------------------------------
#figure(2)
    print( '(phase collib): Start scan ...');

# unblock laser -----------------------------------------------------------

    ddd_write = pydooc.swrite([addr_cam+'TRIGGERDELAYABS'], 0.0);
    print(' - changed camera delay back');
    pause(1)

# turn XTDS on: -----------------------------------------------------------
    tmp      = pydoocs.write(addr.xtds_onoff, 1);

    for jj in range(num_sig):
        
        ### read actuator readback
        ddd_read                = pydoocs.read(addr_actuator_rbv);
        scan_list_rbv[ii,jj]    = ddd_read['data'];

        ## read spectrum x
        ddd_read                = pydoocs.read([addr.camera+ 'SPECTRUM.X.TD']);
        raw_spec_x[ii,jj,:]     = ddd_read['d_gspect_array_val'];
        # compared it with last measurement
        datatimestamp[jj]         = ddd_read['timestamp'];
        # compared it with last measurement
        if jj > 1:
            while datatimestamp[jj] == datatimestamp[jj-1]:

                ddd_read            = pydoocs.read([addr.camera+'SPECTRUM.X.TD']);
                raw_spec_x[ii,jj,:] = ddd_read['d_gspect_array_val'];
                print( '(): same data ... wait ...');
                pause(1/rep_rate)


        # remove bg x
        # corr_spec_x(ii,jj,:)    = hlc_clean_line( squeeze(raw_spec_x(ii,jj,:)) )
        tmp                     = np.squeeze(raw_spec_x[ii,jj,:]);
        corr_spec_x[ii,jj,:]    = tmp' - bgr_spec_x_mean;

        # filter (mean), fit (asymmetric gauss) and position (from fit)
        #tmp                     = medfilt1(corr_spec_x(ii,jj,:), 3);
        #tmp                     = util_gaussFit(1:length(tmp), tmp, 1, 1);
        #pos_CoM_x(ii,jj)        = tmp(2);


        







do_time_collibration(1,2)
