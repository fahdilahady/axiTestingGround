# AXI TESTING GROUND
## Quest 13 Create API automations
### User Stories:
1. As a user, I want to create a product with data : {"name":"string", "description":"string","image":"string","price":integer,"status":false"}
2. As a user, I want to see the details of a product that I recently create.
3. As a user, I want to update the products that I recently created to include {"discount_amount":integer,"status":"true"}
4. As a user, I want to delete the products that I recently updated.

### Dependencies
1. Python
2. Python Request (pip install request)
3. Pytest (pip install pytest)

### Step to run
1. install all dependency
2. cd to Quest13_API_testing directory using CLI
3. run command pytest -v

## Quest 14 Create End to End UI Automation
### User Stories:
1. As a user, I want to login to gist.github.com
2. As a user, I want to create a gist
3. As a user, I want to see the list of gists
4. As a user, I want to delete a gist
5. As a user, I want to edit a gist
6. As a user, I want to logout from gist.github.com

## Dependencies
1. Selenium  (pip install selenium)