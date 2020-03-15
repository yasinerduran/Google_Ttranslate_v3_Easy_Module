from distutils.core import setup
from version import __version__ # version.py dosyasindan __version__ degiskenini al
url = "https://github.com/Akaame/Intervalt" # github linki
version = __version__

setup(name="Google_Ttranslate_v3_Easy_Module",  # Proje ismi
      version=version, # versiyonu
      description="This module wrote for official Google Cloud API for Python.", # aciklama
      long_description="This module wrote for official Google Cloud API for Python. ", # uzun aciklama
      author="Yasin Erduran", # yazar
      url=url, # linki
      license='MIT', # lisansi
      # download_url=url+"/archive/"+version+".tar.gz", # Tagging konusunda daha sonra deginecegiz
      author_email="yasin.herduran@gmail.com", # e-posta
      classifiers=[
          'Development Status :: 0.1.1 - Development/Developmental Release',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ], # bu kisim indeksler tarafindan siniflandirmak amaciyla kullanilir.
      packages=["."] # sunulan paketlerin listesi find_packages komutuyla otomatize edilebilir.
      )