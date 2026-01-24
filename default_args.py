def config():
    defaults = {}
    defaults['predType'] = 'NN_Eq'
    defaults['projType'] = 'H_Bis'
    defaults['probType'] = 'convex_qcqp'
    defaults['probSize'] = [100, 50, 50, 10000]
    defaults['testSize'] = 1024
    defaults['saveAllStats'] = False
    defaults['resultsSaveFreq'] = 1000
    defaults['seed'] = 2025

    defaults['mapping_para'] = \
        {'training': True, 'testing': False, 'n_samples': 1024, 't_samples': 10000, 'bound': [0, 1], 'scale_ratio': 1, 'shape': 'square', 'total_iteration': 20000, 'batch_size': 512, 'num_layer': 3, 'lr': 0.0001, 'lr_decay': 0.9, 'lr_decay_step': 1000, 'penalty_coefficient': 10, 'distortion_coefficient': 1, 'transport_coefficient': 0, 'testing_samples': 1024}

    defaults['nn_para'] = \
        {'training': True, 'testing': True, 'approach': 'unsupervise', 'total_iteration': 10000, 'batch_size': 512, 'lr': 0.001, 'lr_decay': 0.9, 'lr_decay_step': 1000, 'num_layer': 3, 'objWeight': 0.1, 'softWeightInEqFrac': 10, 'softWeightEqFrac': 10}

    defaults['proj_para'] = \
        {'useTestCorr': False, 'corrMode': 'partial', 'corrTestMaxSteps': 100, 'corrBis': 0.9, 'corrEps': 1e-05, 'corrLr': 1e-05, 'corrMomentum': 0.1}

    return defaults
