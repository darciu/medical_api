# medical_api

Command used for building docker image:<br>
<code>docker build -t "medical_api" --secret id=my_env,src=.env .</code><br>
Be aware that credentials for Snowflake connector are not included in the project (they are stored locally).

You can run application locally by running docker image with a command: <br>
<code> docker run -d --name medicalapicontainer -p 8000:8000 medical_api </code><br>
and go to *localhost:8000/docs#/* for app documentation in your browser.

There are four endpoints you can test both using **local** stored data (csv files inside docker) or by connecting **remote**ly Snowflake database via connector:
* Average cost of prescriptions (Gross Cost) in the selected period (month resolution)
* Average number of products (Total Items) in the selected period (month resolution)
* Number of prescriptions in the selected period (month resolution) according to the code (BNF Code)
* Product description (VMP_NM) based on the code (BNF Code)
