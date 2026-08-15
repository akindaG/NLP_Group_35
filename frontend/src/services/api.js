const API_URL = "http://127.0.0.1:8000";


export async function analyzeTicket(text){


    try{


        const response = await fetch(

            `${API_URL}/predict/`,

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


        if(!response.ok){

            throw new Error(
                "Prediction request failed"
            );

        }


        const data = await response.json();


        return data;



    }

    catch(error){

        console.error(
            "API Error:",
            error
        );


        throw error;

    }


}