import React from 'react';
import './home.css';
import { findAllUsers } from '../services/UserService';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUtensils } from '@fortawesome/free-solid-svg-icons';

class HomeComponent extends React.Component {

    state = {
        users: [],
        selectedUser: '',
        chosenUser: false,
        selectedRec: '',
        chosenRec: false
    }

    // Query server (Neo4J) for recommendation for
    // the selected user
    getRecommendedDish(user_id, rec_type) {

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
                            <option value="Recommendation 1">By Friends</option>
                            <option value="Recommendation 2">By Restaurant</option>
                            <option value="Recommendation 3">By Genre</option>
                        </select>
                    </React.Fragment>
                    }

                    {this.state.chosenRec &&
                    <button className="button-rec">
                        Find the perfect food for me!
                    </button>
                    
                    }
                </div>
            </div>
        )
    }
}

export default HomeComponent;