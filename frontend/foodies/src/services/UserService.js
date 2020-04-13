import { API_USER_URL } from "../constants";

/**
* Retrieves all user instances as an array of users.
*/
export const findAllUsers = async () => {
    const response = await fetch(API_USER_URL);
    return await response.json();
}


/**
 * Retrieves recommendation for dishes in the same restaurant based on users who also like what this user likes.
 */
export const findSimilarUserDishRecommendation = async (id) => {
    return await fetch(`${API_USER_URL}/${id}/recommendation_1`)
        .then(response => response.json())
}

/**
 * Retrieves recommendation for dishes in the same restaurant based on the category of the dish this user likes.
 */
export const findSimilarCategoryDishRecommendation = async (id) => {
    return await fetch(`${API_USER_URL}/${id}/recommendation_2`)
        .then(response => response.json())
}

/**
 * Retrieves recommendation for dishes in the same restaurant based on the friends of this user.
 */
export const findDishFriendsRecommendation = async (id) => {
    return await fetch(`${API_USER_URL}/${id}/recommendation_3`)
        .then(response => response.json())
}
