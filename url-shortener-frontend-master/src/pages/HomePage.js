
import React, { useContext, useState, useEffect } from 'react'


import { Link } from 'react-router-dom'
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Unstable_Grid2';

import PacmanLoader from "react-spinners/PacmanLoader";




const HomePage = () => {

  const [input, setInput] = useState("")
  const [code, setCode] = useState("")
  const [loaded, setLoaded] = useState(false)


  let uploadLink = async (e)=> {
    e.preventDefault()
    
       let response =  await fetch('http://127.0.0.1:8000/post-link', {
           method: "POST",
           credentials: "include",
           headers: {
          "Content-Type": "application/json"
     },
             
           body:JSON.stringify({
              "target_url": input,
          })
       })
      
       let data = await response.json()
       setCode(data.encoded)
       console.log(data.encoded)
       

       //setHoverPrice(data)
      
       console.log('response:', response)
       setLoaded(true)

   }
    

    return (
        <div>
          
        
        <header>
            <ul>
             <li><a class="links" href="#user"><button class="signbutton" type="button">Contact Shaphat</button></a></li>
              <li><a href="#images">About</a></li>
              <li><a href="#gmail">Gmail</a></li>
              </ul>  
        </header>
        <div class="logo">
          <h1>URL SHORTENER</h1>
        </div>
        <div>
        <form onSubmit={uploadLink}>
        <div class="bar">
          <input class="searchbar" type="text" title="Search"  value = {input}  onChange={(e) => setInput(e.target.value )} />
    
        </div>
        <div class="buttons">
          <input class="button" type="submit" value="Generate Short Url"/>
          
         </div>
         </form>
         {loaded ? <h2>http://127.0.0.1:8000/{code }</h2> : null}
         </div>
    
         <br/><br/>
       
    
         <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={2} columns={16}>
           
            <Grid xs={8}>
             
              
              
              
            </Grid>
          </Grid>
        </Box>
                
            </div>

    )
}
export default HomePage