function DevPortal() {
    const refreshDB = () => {
        window.alert("DB successfully refreshed!");
    }
    return(
        <div>
            <h1> Dev tools </h1>
            <button onClick={() => refreshDB()}> Refresh database </button> <br />
            <button> Delete database </button> 
        </div>
    )
}

export default DevPortal;