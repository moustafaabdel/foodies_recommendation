import { API_USER_URL } from "../constants";

/**
* Retrieves all user instances as an array of users.
*/
export const findAllUsers = async () => {
    const response = await fetch(API_USER_URL);
    return await response.json();
}