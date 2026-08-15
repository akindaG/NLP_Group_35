import { useState } from "react";
import { motion } from "framer-motion";

import {
    Brain,
    Sparkles,
    Activity,
    Send,
    ShieldCheck,
    BarChart3
} from "lucide-react";


import { analyzeTicket as predictTicket } 
from "../services/api";


import PipelineStatus from "../components/PipelineStatus";
import PredictionCard from "../components/PredictionCard";




function Analyzer(){


const [ticket,setTicket] = useState("");

const [loading,setLoading] = useState(false);

const [analyzed,setAnalyzed] = useState(false);

const [prediction,setPrediction] = useState(null);

const [error,setError] = useState("");





const analyzeTicket = async()=>{


if(!ticket.trim()){

return;

}



try{


setLoading(true);

setAnalyzed(false);

setError("");



const result = await predictTicket(ticket);



console.log(
"AI Prediction Result:",
result
);



setPrediction(result);



setLoading(false);

setAnalyzed(true);



}


catch(err){


console.error(
err
);



setError(
"AI service unavailable. Check backend connection."
);



setLoading(false);



}


};







const models=[


{
name:"XGBoost",
task:"Ticket Classification",
accuracy:"91.8%"
},


{
name:"TF-IDF NLP",
task:"Text Feature Extraction",
accuracy:"95%"
},


{
name:"Prediction Engine",
task:"Enterprise Routing",
accuracy:"92.6%"
}



];






return (



<section

className="
min-h-screen
bg-[#050816]
text-white
pt-28
pb-20
"


>



<div

className="
max-w-7xl
mx-auto
px-6
"

>





{/* HEADER */}



<motion.div


initial={{
opacity:0,
y:30
}}


animate={{
opacity:1,
y:0
}}


className="
mb-10
"


>


<div

className="
inline-flex
items-center
gap-2
px-4
py-2
rounded-full
bg-blue-500/10
border
border-blue-500/30
text-blue-400
text-sm
"

>

<Sparkles size={16}/>

AI Ticket Intelligence Engine


</div>





<h1

className="
text-5xl
font-bold
mt-6
"

>

Enterprise AI Analyzer

</h1>



<p

className="
text-slate-400
mt-4
text-lg
"

>

Real-time NLP powered customer support ticket intelligence.

</p>


</motion.div>









{/* INPUT + PIPELINE */}



<div

className="
grid
lg:grid-cols-2
gap-8
"


>





{/* INPUT CARD */}



<motion.div

className="
bg-white/5
border
border-white/10
rounded-3xl
p-8
backdrop-blur-xl
"


>



<div

className="
flex
items-center
gap-3
mb-6
"

>


<Brain

className="
text-blue-400
"

/>



<h2

className="
text-xl
font-semibold
"

>

Customer Ticket

</h2>


</div>







<textarea


value={ticket}


onChange={
(e)=>setTicket(e.target.value)
}


placeholder="
Example:
My payment failed and I cannot complete transaction
"


className="
w-full
h-52
bg-slate-900
border
border-white/10
rounded-xl
p-5
outline-none
resize-none
focus:border-blue-500
"




/>







<button


onClick={analyzeTicket}


disabled={loading}


className="
mt-6
w-full
py-4
rounded-xl
bg-blue-600
hover:bg-blue-500
disabled:bg-blue-900
flex
items-center
justify-center
gap-3
font-semibold
transition
"

>


{

loading ?


<>

<Activity

className="
animate-spin
"

/>


Running AI Pipeline...


</>


:

<>

<Send size={18}/>


Analyze Ticket


</>


}



</button>







{

error && (


<p

className="
mt-4
text-red-400
text-sm
"

>

{error}

</p>


)


}





</motion.div>









{/* PIPELINE */}



<PipelineStatus />






</div>













{/* MODEL PERFORMANCE */}




<div

className="
mt-10
grid
md:grid-cols-3
gap-6
"

>


{

models.map(model=>(



<div

key={model.name}


className="
bg-white/5
border
border-white/10
rounded-2xl
p-6
"


>


<div

className="
flex
items-center
gap-3
"

>


<Brain

className="
text-blue-400
"

/>


<h3

className="
font-semibold
"

>

{model.name}

</h3>


</div>






<p

className="
text-sm
text-slate-400
mt-4
"

>

{model.task}

</p>





<h2

className="
text-3xl
font-bold
text-blue-400
mt-3
"

>

{model.accuracy}

</h2>





<div

className="
mt-4
h-2
bg-slate-800
rounded-full
overflow-hidden
"

>


<div

className="
h-full
bg-blue-500
"

style={{
width:model.accuracy
}}


/>


</div>



<p

className="
text-green-400
text-xs
mt-3
"

>

● Production Ready

</p>


</div>


))


}



</div>









{/* RESULT */}




{

analyzed && prediction && (


<>


<PredictionCard

data={prediction}

/>







<div

className="
mt-10
bg-purple-500/10
border
border-purple-400/20
rounded-3xl
p-8
"

>


<h2

className="
flex
items-center
gap-3
text-xl
font-bold
mb-5
"

>


<BarChart3

className="
text-purple-400
"

/>


AI Explainability Engine


</h2>






<p

className="
text-slate-400
mb-5
"

>

Important keywords influencing prediction:

</p>





<div

className="
flex
flex-wrap
gap-3
"

>



{

prediction.keywords?.map(
(word)=>(


<span

key={word}

className="
px-4
py-2
rounded-full
bg-purple-500/20
border
border-purple-400/20
text-purple-300
"

>

{word}

</span>


)


)


}





</div>







<div

className="
mt-6
flex
items-center
gap-2
text-green-400
"

>


<ShieldCheck size={18}/>


Explainable prediction generated


</div>



</div>



</>


)

}






</div>


</section>



)

}


export default Analyzer;