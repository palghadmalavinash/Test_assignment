# Test_assignment
Steps to Execute testcases:
1. Install the requirements from the requirements.txt documents
   <br><b>pip3 install -r requirements.txt</b>
2. Change the username and password fields in the amazon.feature file
   <br><b>enter the credentails in the login page as '< username >' and '< password >'</b>
3. To run the test case through pycharm,
   <br><b>a. Load project in pycharm.</b>
   <br><b>b. Select Edit Configuration from Run menu.</b>
   <br><b>c. Select + option at the top of the config window.</b>
   <br><b>d. Select Python test ->> Py.test from the dropdown.</b>
   <br><b>e. Select project directory in right side of the window.</b>
   <br><b>f. Enter Keyword as Agrostartes and click apply and ok</b>
   <br><b>G. Select the Run optoin from the top.</b>
4. To run the command from command prompt.
   <br>a. Navigate to the Checkout directory.</b>
   <br>b. Run below command.</b>
   <br><b>pytest -k Agrostartest</b>

<b> Executing API test case:</b>
Follow all the above steps instead of step 2 do:
   <br> Change the access_token in config.ini file
