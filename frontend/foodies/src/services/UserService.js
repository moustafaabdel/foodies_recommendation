import { API_USER_URL } from "../constants";

/**
* Retrieves all user instances as an array of users.
*/
export const findAllUsers = async () => {
    const response = await fetch(API_USER_URL);
    return await response.json();
}


/**
 * Retrieves recommendation for dishes in the same restaurant based on the given user and similar users.
 */
export const findSimilarUserDishRecommendation = async (id) => {
    return await fetch(`${API_USER_URL}/${id}/recommendation_1`)
        .then(response => response.json())
}

/**
 * Retrieves user's favorite dish (and its restaurant)
 */
export const findUserFavorites = async (id) => {
    return await fetch(`${API_USER_URL}/${id}/favorites`)
        .then(response => response.json())
}