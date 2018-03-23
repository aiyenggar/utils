#conda install anaconda-clean
#anaconda-clean --yes

PWD=`pwd`
cd ~
rm -rf anaconda
rm -rf .anaconda_backup
rm -rf .spyder*

cd /Applications
rm -rf anaconda
rm -rf Anaconda-Navigator.app

cd $PWD
