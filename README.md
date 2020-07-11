Set up Instruction as follows:
---------------------------------
1. Get python 3
2. inside maxProfitMovies directory run following commands:<br/>

   <b>a.</b>  py -m venv env_movie <br/>
   <b>b.</b>  .\env_movie\Scripts\activate <br/>
   <b>c.</b>  pip install -r requirements.txt<br/>
   <b>d.</b>  python app.py<br/>
   
Now server is up and running:

Api end-point
-----------------
/movies_api/v1/movies (POST)

Testing using postman
----------------------
http://127.0.0.1:5000/movies_api/v1/movies

**Note: Its runnig on PORT:5000, in your case it might differ

![image](https://user-images.githubusercontent.com/9819281/87231246-25540300-c3d3-11ea-939a-b6d5561d65b4.png)

Response:

![image](https://user-images.githubusercontent.com/9819281/87231269-63e9bd80-c3d3-11ea-9638-397e7a020ba5.png)
