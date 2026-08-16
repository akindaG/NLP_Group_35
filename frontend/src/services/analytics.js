const API_URL = "http://127.0.0.1:8000";


export async function getAnalytics(){

    const response = await fetch(
        `${API_URL}/analytics/`
    );


    if(!response.ok){

        throw new Error(
            "Analytics API failed"
        );

    }


    return await response.json();

}