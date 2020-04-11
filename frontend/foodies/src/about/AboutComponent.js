import React from 'react';
import './about.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUtensils } from '@fortawesome/free-solid-svg-icons';

const AboutComponent = () => {

    return(
        <div>
            <div className='navbar'>
                <div className='link'><a className='link-text' href='/'>Home</a></div>
                <div className='link'><a className='link-text' href='/about'>About</a></div>
            </div>
            <div className='main-header container'>
                    <h1 className='headline'>about <FontAwesomeIcon icon={faUtensils}/> </h1>
                    <div className='about-text'>
                        <p>This is a minimalist food recommendation system highlighting the capabilities of graph databases by 
                            recommending dishes to try at particular restaurants. The frontend is written in React, the backend in 
                            Flask/Python, and the database is Neo4J.</p>
                        <p>While this food recommendation system does offer the capability to recommend food based on
                            metrics such as what your friends enjoy (similarly to other popular food recommendation services), 
                            this recommendation system also utilizes how metrics such as the dishes you like, restaurants you like, 
                            and the genres of food you like and how they may be similar to other people's tastes. Then, we 
                            utilize that commonality to provide you with new options of food to try!</p>
                        <p>Completed as a project by Kristi Bui, Moustafa Abdelaziz, Aasish Basani, and 
                            Vidhi Gondalia for Spring 2020 DS4300 (Large Scale Information, Storage and Retrieval) at Northeastern
                            University.</p>
                    </div>
            </div>
        </div>
    )
};

export default AboutComponent;