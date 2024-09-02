# Interface Specification Document

![Question5Img](https://i.ibb.co/QM0Z6yZ/c2f1cb7e-5022-433a-93a2-1ac0b6ec1015.png)

## Overview

This document explains how the user management screen should function. Our goal is to provide a practical interface where administrators can easily add and edit users, assign roles, and activate or deactivate accounts. The document outlines how to sort and filter the user list, what information is required when adding a new user, and the overall behavior of the interface step by step. Our objective is to make user management simple and understandable for everyone.


## 1. Interface Components

### 1.1. **User List Table**
- **Location**: Left side of the interface.
- **Description**: Displays a list of existing users within the system.
- **Columns**:
  - **ID**: Unique identifier for each user.
  - **User Name**: The username assigned to the user.
  - **Email**: The email address associated with the user.
  - **Enabled**: Indicates whether the user account is active (`true`) or inactive (`false`).

- **Features**:
  - **Sorting**: Each column can be sorted in ascending or descending order by clicking the header.
  - **Filtering**: Users can filter the list based on user attributes such as ID, Username, Email, or Enabled status.

### 1.2. **New User / User Details Form**
- **Location**: Right side of the interface.
- **Description**: Used for creating new users or editing the details of existing users.

- **Fields**:
  - **Username**: Input field for the user’s username. _(Required)_
  - **Display Name**: Input field for the user's display name. _(Optional)_
  - **Phone**: Input field for the user's phone number. _(Optional)_
  - **Email**: Input field for the user's email address. _(Required)_
  - **User Roles**: Dropdown menu for selecting one or multiple user roles.
    - **Options**:
      - Guest
      - Admin
      - SuperAdmin
  - **Enabled**: Checkbox to indicate if the user account should be active.

- **Buttons**:
  - **Save User**: Located at the top-right. Saves the user details and updates the user list table.
  - **New User**: Located at the top-left. Clears the form and allows the creation of a new user.

### 1.3. **Hide Disabled User Checkbox**
- **Location**: Above the User List Table.
- **Description**: A checkbox that, when selected, hides all users with the "Enabled" status set to false from the User List Table.


## 2. Page Behavior

### 2.1. **Initial Load**
- Upon initial load, the User List Table displays all users with their corresponding details.
- The form on the right side is cleared and ready for new user input.
- The "Hide Disabled User" checkbox is unchecked by default, showing both active and inactive users.

### 2.2. **User Selection**
- When a user clicks on a row in the User List Table, the details of that user populate the form fields on the right side.
- Changes made to the form can be saved by clicking the "Save User" button, which will update the existing user details in the User List Table.

### 2.3. **New User Creation**
- Clicking the "New User" button clears the form on the right, enabling input for a new user.
- After filling out the form, clicking "Save User" will add the new user to the User List Table and refresh the list.

### 2.4. **Filtering and Sorting**
- Users can filter or sort any column in the User List Table to locate specific users easily.
- The "Hide Disabled User" checkbox can be used in conjunction with the sorting and filtering options.

### 2.5. **User Roles Dropdown Behavior**
- The "User Roles" dropdown allows for the selection of multiple roles.
- If a role is selected, it remains highlighted, and additional roles can be added or removed.

### 2.6. **Form Validation**
- Required fields ("Username" and "Email") must be validated before the form can be submitted.
- If a required field is missing, an error message will be displayed, and the form will not submit.

### 2.7. **Saving Data**
- Clicking "Save User" will trigger the following:
  - Form validation.
  - If valid, the data will be sent to the server to update the user list.
  - The User List Table will refresh to reflect the new or updated user data.


## 3. Display Requirements

- The User Management Interface should be responsive, ensuring usability across different devices and screen sizes.
- All text should be clearly visible with sufficient contrast against the background.
- The form layout should adapt to the content, expanding as necessary to accommodate longer text inputs.
- Error messages should be displayed inline with the corresponding input field to enhance user understanding.
- 
## 4. User Interaction Scenarios

### Scenario 1: Creating a New User
1. User clicks the "New User" button.
2. The form clears, and the user enters the required information.
3. The user selects appropriate roles from the "User Roles" dropdown.
4. The user checks the "Enabled" checkbox if the user account should be active.
5. The user clicks the "Save User" button.
6. The new user appears in the User List Table.

### Scenario 2: Editing an Existing User
1. User selects an existing user from the User List Table.
2. The user updates the desired fields in the form.
3. The user clicks the "Save User" button.
4. The updated details are reflected in the User List Table.

### Scenario 3: Filtering Users
1. User checks the "Hide Disabled User" checkbox.
2. The User List Table updates to show only active users.
3. User sorts or filters columns as needed to locate specific users.