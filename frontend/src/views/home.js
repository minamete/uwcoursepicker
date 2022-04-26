import {useState, useEffect} from 'react';

function HomePage() {
    const [response, setResponse] = useState('');
   /* useEffect(() => {
        callAPI();
    }, [])

    function callAPI() {
        fetch("http://localhost:9000/testAPI")
            .then(res => res.text())
            .then(res => setResponse(res));
    }*/

    
    return(
        <div>
            {/*response*/}

        </div>
    )
}

export default HomePage;