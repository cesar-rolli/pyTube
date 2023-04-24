import React, {useEffect, useState} from 'react';
import axios from "axios";
import './App.css';

function App() {
  const [initialData, setInitialData] = useState([{}]);
  const [link, setLink] = useState([{}]);
  
  // receber
  useEffect(() => {
    fetch('/api')
    .then(response => response.json())
    .then(data => setInitialData(data))
  }, []);
  
  // enviar
  const [inputs, setInputs] = useState([]);
  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }
  
  const handleSubmit = (event) => {
    event.preventDefault();

    axios.post('/submit', inputs)
    .then(function(response){
      console.log(response.data);
    });
  };

  return (
    <div className="App">
      <form className="column"
        onSubmit={handleSubmit}>
        <div className="row">
          <p>YouTube link:</p>
          <input 
            type="text" 
            name="link" 
            className="input"
            onChange={handleChange}
            />
        </div>
        <div className="row">
          <p>Resolution:</p>
          <p className="radio"><input type="radio" value="720p" name="resolution" onChange={handleChange}/>720p (HD)</p>
          <p className="radio"><input type="radio" value="1080p" name="resolution" onChange={handleChange}/>1080p (FHD)</p>
          <p className="radio"><input type="radio" value="2160p" name="resolution" onChange={handleChange}/>2160p (4K)</p>
          <p className="radio"><input type="radio" value="4320p" name="resolution" onChange={handleChange}/>4320p (8K)</p>
        </div>
        <button name="submit" className="button">Download</button>
      </form>
      <div className="list">
      </div>
    </div>
  );
}

export default App;
