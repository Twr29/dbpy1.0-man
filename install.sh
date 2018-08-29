echo "Welcome to Installer Python mysql-connector"
choose()
{
 echo -n "You want to install mysql-connector ?(y/n) : "
 read choose
 if [ $choose == "y" -o $choose == "Y" ]
 then
	based()
	{ echo -n "What your linux Based ? (Debian/Arch/Redhat) : "
      	  read base
	  if [ $base == "D" -o $base == "d" ]
	  then
		sudo apt-get update
		sudo apt-get install python3.7 && sudo apt-get install python-pip
		echo "Process for Install Mysql-Connector..."
        	python -m pip install mysql-connector
        	echo "mysql-connector Success for Install."
	  elif [ $base == "A" -o $base == "a" ]
	  then
		sudo pacman -Syu
		sudo pacman -S python3.7 
		sudo pacman -S python-pip
		echo "Process for Install Mysql-Connector..."
        	python -m pip install mysql-connector
        	echo "mysql-connector Success for Install."
	  elif [ $base == "R" -o $base == "r" ]
	  then 
		sudo yum -y update
		sudo yum -y install python3.7
		sudo yum -y install python-pip
		echo "Process for Install Mysql-Connector..."
        	python -m pip install mysql-connector
        	echo "mysql-connector Success for Install."
	  else
		echo "Your input invalid, Enter valid Input.........."
		based
	  fi
	}
	based
 elif [ $choose == "n" -o $choose == "N" ]
 then
  	echo "You not Install mysql-connector. "
 else
  	echo "Your input invalid, Enter valid input......."
	echo ""
	choose
 fi
}
choose
