
import kaggle as kg
kg.api.authenticate()
kg.api.dataset_download_files(dataset='somesnm/partynyc', path='.', unzip=True, force=True)





