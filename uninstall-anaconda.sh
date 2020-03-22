#conda install anaconda-clean
#anaconda-clean --yes

PWD=`pwd`
cd ~
rm -rf .anaconda_backup
rm -rf .spyder*
rm -rf .anaconda/navigator
rm -rf .condarc .conda .continuum
rm -rf .matplotlib .ipython
rm -rf anaconda
#nano ~/.bash_profile # remove the anaconda directory from your `PATH` env var

echo "In Applications"
cd /Applications
echo "Deleting anaconda"
rm -rf anaconda3
rm -rf Anaconda-Navigator.app

cd $PWD
