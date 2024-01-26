def do_time_collibration(min, max):
    import doocs_address as addr
    import time
    import numpy as np
    import pydoocs
    #from datetime import date
    from datetime import datetime
    import scipy.signal as sg
    from scipy.optimize import curve_fit
    #print(addr.TDSphase)
    fontSize        = 14;
    num_actuator=6;
    num_bgr=10;
    num_actuator=5;
    delay = pydoocs.read(addr.camera 'TRIGGERDELAYABS')['data'];
    #pixelformat=doocswrite(addr.camera 'FORMAT.OUT')['data']; #until IAS is used:...
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
    ddd_write = pydoocs.write((addr.camera+'ROI_SPECTRUM.ON'), 0);
    ddd_write = pydoocs.write((addr.camera+'ROI2_SPECTRUM.ON'), 0);
# switch off: BG subtraction -----------------------------------------------------------
    ddd_write = pydoocs.write((addr.camera+'SUBSTR.ON'), 0);
# switch on spectrum
    ddd_write = pydoocs.write((addr.camera+'SPECTRUM.ON'), 1);

## prepare data structure -----------------------------------------------------------
    ddd_read        = pydoocs.read(addr.camera+'IMAGE_EXT');
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

    ddd_write = pydoocs.write(addr_cam+'TRIGGERDELAYABS', 1000);
    print(' - changed camera delay');
    time.sleep(2)
###################### Should be fixed -----------------------------------------------------------
# take bgr
    bgr_spec_x_mean = take_spectrum_data(num_bgr, 1/rep_rate)
    # take one img
    ddd_read        = doocsread([addr_cam, 'IMAGE_EXT']);
    bgr_img         = ddd_read['val_val'];

    ## scan loop -----------------------------------------------------------
#figure(2)
    print( '(phase collib): Start scan ...');

# unblock laser -----------------------------------------------------------

    ddd_write = pydooc.swrite([addr_cam+'TRIGGERDELAYABS'], 0.0);
    print(' - changed camera delay back');
    time.sleep(1/rep_rate)

# turn XTDS on: -----------------------------------------------------------
    tmp      = pydoocs.write(addr.xtds_onoff, 1);

    for ii in range(num_actuator): #scan points
         # set value
         ddd_write = pydoocs.write(addr_actuator_set, scan_list_set[ii]);
         #print( ' Set actuator ', name_actuator, ' to ' , num2str(scan_list_set(ii), '%5.3f')]);

    # wait for set = rbv
        print('Actuator name_actuator set')
        time.sleep(1/rep_rate)
        ### read actuator readback
        ddd_read                = pydoocs.read(addr_actuator_rbv);
        scan_list_rbv[ii]    = ddd_read['data'];


        # remove BG
        tem=take_spectrum_data(num_sig, 0)
        raw_spec_x=tmp - bgr_spec_x_mean
            # filter
        raw_spec_x=sg.medfilt(raw_spec_x)
        popt, pcov = curve_fit(gaussian, range(1, len(raw_spec_x)+1), raw_spec_x)
        x0_fit, sigma_fit = popt
        pos_CoM_x[ii]  = x0_fit

        corr_spec_x=np.append(corr_spec_x,[raw_spec_x], axis=0)


# plot


        # remove bg x
        # corr_spec_x(ii,jj,:)    = hlc_clean_line( squeeze(raw_spec_x(ii,jj,:)) )
        tmp                     = np.squeeze(raw_spec_x[ii,jj,:]);
        corr_spec_x[ii,jj,:]    = tmp' - bgr_spec_x_mean;

        # filter (mean), fit (asymmetric gauss) and position (from fit)
        #tmp                     = medfilt1(corr_spec_x(ii,jj,:), 3);
        #tmp                     = util_gaussFit(1:length(tmp), tmp, 1, 1);
        #pos_CoM_x(ii,jj)        = tmp(2);

def take_spectrum_data(iteration, rest_time):
    import doocs_address as addr
    import numpy as np

    ddd_read= pydoocs.read(addr.camera+'SPECTRUM.X.TD');
    x=[ddd_read['data']]
    datatimestamp= ddd_read['timestamp']

    datatimestamp=np.zeros(iteration)
    for jj in range(1,iteration):

        # read x
        ddd_read            = pydoocs.read(addr.camera+'SPECTRUM.X.TD');
        x       = np.append(x, [ddd_read['data']], axis=0);
        datatimestamp   =np.append(datatimestamp, ddd_read['timestamp']);
        print(jj)
        ## compared it with last measurement -----------------------------------------------------------

        while datatimestamp[jj] == datatimestamp[jj-1]:
            ddd_read        = pydoocs.read(addr.camera+'SPECTRUM.X.TD');
            x       = np.append(x, [ddd_read['data']], axis=0);
            datatimestamp   =np.append(datatimestamp, ddd_read['timestamp']);
            print( ' same data ... wait ...');
            time.sleep(rest_time)
        ####read y

        # compute mean()
    spec_x_mean = np.mean(x,0);
    return spec_x_mean

def gaussian(x, x0, sigma):
   return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - x0) ** 2) / (2 * sigma** 2))






do_time_collibration(1,2)
