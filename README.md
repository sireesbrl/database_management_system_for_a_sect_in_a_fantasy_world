# Database Management System for a Sect in a Fictional World

#### Video Demo:  [watch here!](https://www.youtube.com/watch?v=bK819YckFMs)

#### Description:
Generally, in a cultivation novel, there are many sects fighting for resources. A sect may contain thousands of disciples of various levels with different profession working to better themselves. To make it easier for proper management of human and material resources in a sect, it is done best with the existence of a database management system. This python program makes it easier for higher authorities of a sect to add, read, update and delete data of various disciples in the sect. Disciple too can use this program to get details of various cultivation levels and different profession they can choose. For the purpose of an example, the "Cosmic Star Academy" has installed this program in their system for management purposes. The initial welcome banner can be changed according to the user's need.

Users of this program can create a new account with different permissions if they don't already have an account. Some of the default usernames and their password for testing purposes are listed below:

#### Default Usernames and Passwords

##### For Sect Master:
* **Username**: test1
* **password**: test1
* **permissions**: Read, Write, Edit and Delete

##### For Vice-Sect Master:
* **Username**: test2
* **password**: test2
* **permissions**: Read, Write and Edit

##### For Sect-Protector:
* **Username**: test3
* **password**: test3
* **permissions**: Read and Write

##### For Disciple:
* **Username**: test4
* **password**: test4
* **permissions**: Read


#### Brief description of the options available:

* **Info on Cultivation Levels**:

    Gives basic knowledge of cultivation levels and what kind of transformation to expect and work towards.

* **Info on Professions**:

    Gives basic knowledge on different types of professions.

* **Add New Disciples**:

    Add details of a disciples into database for future reference like Name, Type of Disciple, Profession, Department and Cultivation Law. The data of disciples is stored in a csv file as key-value pairs using csv.DictWriter() function from the csv module.

* **Read Data of Disciples**:

    Displays the details stored in database in a tabular view. The data of disciples is read using csv.DictReader() function from the csv module.

* **Update Data of Disciples**:

    Change entries of a disciple and update it to the database. To implement an update/edit function, data in the csv file is read to a list of dictionaries which is updated as required and written to the file in write mode to re-write the whole of csv file to make it a less complex process as only a small amount of data is worked on in this program.

* **Delete Data of Disciples**:

    Delete the data of a disciple in the database. Implementation of this function is similar to the update function where we re-write the csv file without the entry/list of entries to be deleted.

* **Log Out**:

    Log out the current user and login any other accounts for the different services provided according to the permissions specified.

* **Exit**:

    Exit the program safely after use.


#### Future Development:
This program can be further expanded to add a recommendation system that recommends different special sites present in the world like Five Elements active regions or any peculiar regions for comprehension of laws according the disciples needs.

The famous forbidden lands in the fictional world where our sect exists according to various elements:

**Forbidden lands**:
* Water -> Endless Ocean
* Earth -> Heavenly Corpse Burial Ground
* Wood -> Nightmare Forest
* Metal -> Divine Dragon Mountain Range
* Fire -> Eternal Fire Gorge
