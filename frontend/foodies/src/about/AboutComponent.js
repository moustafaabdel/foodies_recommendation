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
                        <p>This food recommendation is based around recommending dishes at the same restaurant that servers
                             a user's favorite dish. Specifically, it allows three modes of recommendation: 1. recommend a dish 
                             based on what your friends like, 2. recommend a dish based on those who like your dish also like, and 
                             3. recommend a dish of a similar genre to your favorite dish.</p>
                        <p>Completed as a project by Kristi Bui, Moustafa Abdelaziz, Aasish Basani, and 
                            Vidhi Gondalia for Spring 2020 DS4300 (Large Scale Information, Storage and Retrieval) at Northeastern
                            University.</p>
                    </div>
            </div>
        </div>
    )
};

export default AboutComponent;