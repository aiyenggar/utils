# Print the kth line of a file using sed

# Get the first k lines of a file, in place using sed -i

# To count if there are an odd number (unmatched) double quotes
awk -F\" 'NF % 2 == 0' 

# To drop a certain field (2nd here) in a text file
awk -F"\t" '{ $2=""; print}'

# Print the entire line of a tab separated file if the 4th field mathes “IN”
awk -F"\t" '$4=="IN" {print $0}'  location.tsv > india.location.tsv


# Pattern search anywhere in string
`awk': awk -F"\t" 'tolower($8) ~ /indian space/ {print $2","$8} ‘ rawassignee.tsv

rsync -r ~/personal /Volumes/2013a\ Data/OneDrive --delete


SSH Key Generation
ssh-keygen -t rsa -b 4096 -C "ashwin.iyenggar@gmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
pbcopy < ~/.ssh/id_rsa.pub
paste this on github.com settings
ssh -T git@github.com

Ashwin’s Summary:
mkdir folder, add files
git init
git crypt init
fill in .gitattributes file

* filter=git-crypt diff=git-crypt
/** filter=git-crypt diff=git-crypt
*.csv filter=git-crypt diff=git-crypt
.git* !filter !diff

git crypt status
for existing repos: git crypt status -f (But previous commits will just stay as usual)
git add *
git commit -m “message"
Create the repository on github.com

git remote add origin git@github.com:aiyenggar/summer.git
git push -u origin master

Checking out an existing project
git clone git@github.com:aiyenggar/utils.git

Troubleshooting
Incase the repository was cloned from the desktop app prior to the ssh setting

 git config --global user.name “Ashwin"
 git config --global user.email "aiyenggar@users.noreply.github.com"
git remote set-url origin git@github.com:aiyenggar/econometrics.git

git crypt status
git crypt lock
git crypt unlock

# To get git-crypt, you needed to update xcode from App Store, then download gnutools or something like that. 

The locking unlocking process on git crypt
locking is easy. git crypt lock.
To unlock, you first need to place the default key file into .git/git-crypt/keys/
then git crypt add-gpg-user ashwin.iyenggar@gmail.com
finally you can git crypt unlock

At this stage you can seamlessly lock and unlock without further steps. But if I need to rsync to an external drive in a way that the content is encrypted, then what should I do? Should I delete the .git-crypt folder? Also, what happens if I lose the default key file. What is it, really?

