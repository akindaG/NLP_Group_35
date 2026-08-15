const API_BASE_URL = "http://127.0.0.1:8000";


export async function getHealth() {

    const response = await fetch(
        `${API_BASE_URL}/health`
    );

    if (!response.ok) {
        throw new Error("Backend unavailable");
    }

    return await response.json();
}



export async function getAnalytics() {

    const response = await fetch(
        `${API_BASE_URL}/analytics/`
    );

    if (!response.ok) {
        throw new Error("Analytics unavailable");
    }

    return await response.json();

}



export async function getHistory() {

    const response = await fetch(
        `${API_BASE_URL}/analytics/history`
    );

    if (!response.ok) {
        throw new Error("History unavailable");
    }

    return await response.json();

}



export async function predictTicket(text) {

    const response = await fetch(
        `${API_BASE_URL}/predict/`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                text:text
            })
        }
    );


    if (!response.ok) {
        throw new Error("Prediction failed");
    }


    return await response.json();

}

export async function analyzeTicket(text){

    const response = await fetch(
        `${API_BASE_URL}/predict/`,
        {
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify({
                text:text
            })
        }
    );


    if(!response.ok){
        throw new Error("Analysis failed");
    }


    return await response.json();

}

export async function getPredictionHistory() {

    const response = await fetch(
        `${API_BASE_URL}/analytics/history`
    );


    if (!response.ok) {
        throw new Error("Prediction history unavailable");
    }


    return await response.json();

}