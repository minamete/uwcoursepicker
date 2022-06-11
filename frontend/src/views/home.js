import {useState, useEffect} from 'react';
import CourseCard from '../components/CourseCard';

function HomePage() {
    
    const [courses, setCourses] = useState([]);
    const [dept, setDept] = useState("CS")

    useEffect(() => {
        callAPI();
    }, [dept])


    function callAPI() {
        if (!dept) return;
        fetch("http://localhost:8080/courses/" + dept) // gets a pr
        .then(res => res.json())
        .then(res => setCourses(res));
    }

    
    return(
        <div>
            <input onChange={e => setDept(e.target.value)}></input>
            {courses && courses.map(course => <CourseCard course={course} />)}
        </div>
    )
}

export default HomePage;