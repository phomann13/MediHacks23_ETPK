const fs = require('fs');

// Function to add user login data to a JSON file
function addUserToJSON(userData) {
  // Read the existing JSON data from the file, if it exists
  let jsonData = [];
  try {
    const data = fs.readFileSync('users.json', 'utf8');
    jsonData = JSON.parse(data);
  } catch (error) {
    // If the file doesn't exist or is empty, jsonData will remain an empty array
  }

  // Add the new user data to the array
  jsonData.push(userData);

  // Write the updated JSON data back to the file
  fs.writeFileSync('users.json', JSON.stringify(jsonData, null, 2), 'utf8');
}

// Example user data
const newUser = {
  username: 'exampleUser',
  password: 'examplePassword',
  email: 'user@example.com',
};

// Call the function to add the user data to the JSON file
addUserToJSON(newUser);

console.log('User added to JSON file.');
