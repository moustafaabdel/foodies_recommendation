import React from 'react';
import './home.css';
import { findAllUsers, findSimilarUserDishRecommendation, findSimilarCategoryDishRecommendation, findDishFriendsRecommendation } from '../services/UserService';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUtensils, faFrown } from '@fortawesome/free-solid-svg-icons';

class HomeComponent extends React.Component {

    state = {
        users: [],
        selectedUser: '',
        chosenUser: false,
        selectedRec: '',
        chosenRec: false,
        recommended: []
    }

    // Query server (Neo4J) for recommendation for selected user
    getRecommendedDish(user_id, rec_type) {

        switch(rec_type) {
            case '1':
                findDishFriendsRecommendation(user_id)
                    .then(dish => {this.setState(
                        {recommended: dish}
                    )});
                break;

            case '2':
                findSimilarUserDishRecommendation(user_id)
                    .then(dish => {this.setState(
                        {recommended: dish}
                    )});
                break;

            case '3':
                findSimilarCategoryDishRecommendation(user_id)
                    .then(dish => {this.setState(
                        {recommended: dish}
                    )});
                break;
        }
    }

    componentDidMount = async () => {
        findAllUsers()
            .then(allUsers => {this.setState(
                {users: allUsers}
            )})
    }

    render() {
        return(
            <div>
                <div className='navbar'>
                    <div className='link'><a className='link-text' href='/'>Home</a></div>
                    <div className='link'><a className='link-text' href='/about'>About</a></div>
                </div>

                <div className='main-header container'>
                    <h1 className='headline'>what should you order? <FontAwesomeIcon icon={faUtensils}/> </h1>
                    <span className='description'>A smart food recommendation system for indecisive people.</span>

                    <label htmlFor="people" className="label">First, choose a person to order food for: </label>

                    <select id="people"
                            defaultValue="Select User:"
                            onChange={(e) => {this.setState({
                                selectedUser: e.target.value,
                                chosenUser: true
                            })}}>
                        <option value="Select User:" disabled>Select User:</option>
                        {this.state.users.map(user => 
                        <option 
                            key={user.user_id}
                            value={user.user_id}>User {user.user_id}
                        </option>)}
                    </select>


                    {this.state.chosenUser && 
                    <React.Fragment>
                       <label htmlFor="people" className="label">Now, choose how you'd like to recommend food: </label>
                       <select id="recommendation"
                               defaultValue="Select Method:"
                               onChange={(e) => {this.setState({
                                   selectedRec: e.target.value,
                                   chosenRec: true
                               })}}>
                            <option value="Select Method:" disabled>Select Method:</option>
                            <option value="1">By Friends</option>
                            <option value="2">By Restaurant</option>
                            <option value="3">By Genre</option>
                        </select>
                    </React.Fragment>
                    }

                    {this.state.chosenRec &&
                    <button className="button-rec"
                        onClick={() => {this.getRecommendedDish(this.state.selectedUser, 
                                            this.state.selectedRec)}}>
                        Find the perfect food for me!
                    </button>
                    
                    }

                    {Object.keys(this.state.recommended).length === 3 &&
                    <div className='container'>
                        <span className='recommendation'>
                            Hmmm... this person seems to order <b>{this.state.recommended[0].item}</b> from <b>{this.state.recommended[1].restaurant_name}</b> a lot.
                        </span>

                        {this.state.selectedRec === '1' ? 
                        <span className='recommendation'>
                            Their friends enjoy ordering <b>{this.state.recommended[2].item}</b>.
                        </span>
                        
                        : this.state.selectedRec === '2' ?
                        <span className='recommendation'>
                            Others who like this dish also like ordering <b>{this.state.recommended[2].item}</b>.
                        </span>

                        :
                        <span className='recommendation'>
                            A dish similar to this one is <b>{this.state.recommended[2].item}</b>.
                        </span>
                        }

                    </div>
                    }

                    {Object.keys(this.state.recommended).length === 1 &&
                    <div className='container'>
                        <span className='recommendation'>
                            Uh-oh, looks like we couldn't find a recommendation for this person <FontAwesomeIcon icon={faFrown}/>.
                        </span>
                    </div>
                    }
                </div>
            </div>
        )
    }
}

export default HomeComponent;