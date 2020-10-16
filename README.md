# Using the framework

#### Server setup:

Clone the server repo and start the server
    
    git clone https://github.com/Interview-demoapp/Flasky
    
    On Windows:
       set FLASK_APP=demo_app
       
    On Linux:
       export FLASK_APP=demo_app
    
    flask init-db
    flask run --host=0.0.0.0 --port=8080

#### Running the tests

- ##### UI tests
 
   For UI tests , `robot framework` is used
   Page objects are created , consisting of actions related to respected page in 'ui/pages' dir
   
   Navigate to testing directory

   UI tests are present in the `ui` repo . Tags like `regression`, `registration` and `login`
are created tests   
   
   Running all the UI tests
   
      python -m robot -i regression test_login

   Run login related tests
    
      python -m robot -i regression test_login login
        
   ##### After running the tests results **report.htm**l file is generated consisting of number of tests passed/failed with detailed info. 
 
 
- ##### API tests
    For API tests **Unittest**  is used with  `pytest` is used 
    
    Running the testcases
    
      pytest --html=report.html test/test_api.py 
    
    Result is generated in api/report.html file 
    
------
 
#### Questions
 
1. ##### Code review 
   For code review , make sure that coding standards are enforced. 
   Have comments in the code for explaining the logic. 
   
2. ##### Enforce coding standards
   Should have PEP8 as coding standards in python. User [flake8](https://flake8.pycqa.org/en/latest/) for coding standards enforcement 
 
3. ##### How do you plan what kind of approach you take for test automation - what libraries to use, how does it work in couple of years, how to make it easy to maintain, etc? What are the main points to consider? 
   For UI , we can use `selenium` and `pytest` as main libraries, 
   For API , we can use `request` and `pytest` libraries. 
   
4. ##### Report of found issues/bugs 
    1. There is no validation implemented in the app. Like for password there is no complexity 
    2. In the request password is sent as plaintext in request.
    3. There is no expiration limit to token . 
    4. Token is also not specific to client. I can use the same token from different app.  
    5. 
    
5. ##### Report of found issues/bugs   improvement would you propose for the app 
    There is bug in the application related to `iteritems` it does not work with python3. `data.items()` as it is not supported in python3. 
    
 
