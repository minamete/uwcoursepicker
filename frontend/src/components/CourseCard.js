const CourseCard = ({ course }) => {
    return (
        <div>
            <h1> {course.name} </h1>
            <h2> {course.dept} {course.course_num}</h2>
            <p> {course.desc} </p>
            {course.prereqs != "" && <p> Prereqs: {course.prereqs}</p>}
            {course.coreqs != "" && <p> Coreqs: {course.coreqs}</p>}
            {course.antireqs != "" && <p> Antireqs: {course.antireqs}</p>}
            {course.crosslisted != "" && <p> Crosslisted: {course.crosslisted}</p>}
        </div>
    )
}
export default CourseCard;