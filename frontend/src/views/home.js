import {useState, useEffect} from 'react';

function HomePage() {
    useEffect(() => {
        callAPI();
    }, [])

    function callAPI() {
        fetch("http://localhost:8080/courses")
            .then(res => res.text())
            .then(res => console.log(res));
    }

    
    return(
        <div>
            {/*response*/}

        </div>
    )
}

export default HomePage;