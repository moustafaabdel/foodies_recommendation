import React from 'react';
import { Route, BrowserRouter as Router } from 'react-router-dom';
import HomeComponent from './home/HomeComponent';
import AboutComponent from './about/AboutComponent';
import './App.css';

const App = () => {
  
  return (
    <Router>
      <Route exact path="/" component={HomeComponent}></Route>
      <Route exact path="/about" component={AboutComponent}></Route>
    </Router>
  )
}

export default App;
