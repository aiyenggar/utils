#conda install anaconda-clean
#anaconda-clean --yes

PWD=`pwd`
cd ~
rm -rf anaconda
rm -rf .anaconda_backup
rm -rf .spyder*
rm -rf .anaconda/navigator
rm -rf .condarc .conda .continuum
nano ~/.bash_profile # remove the anaconda directory from your `PATH` env var

cd /Applications
rm -rf anaconda
rm -rf Anaconda-Navigator.app

cd $PWD
