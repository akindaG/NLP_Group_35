import {
    Ticket,
    AlertTriangle,
    Brain,
    Target,
    TrendingUp,
    Clock,
    Cpu,
    ShieldCheck,
    Activity,
    RefreshCw,
    Download
} from "lucide-react";


import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer,
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid
} from "recharts";


import { motion } from "framer-motion";


import {
    getAnalytics,
    getHealth,
    getPredictionHistory
} from "../services/api";


import { useEffect, useState } from "react";





function Dashboard(){


const [analytics,setAnalytics] = useState(null);

const [health,setHealth] = useState(null);

const [history,setHistory] = useState([]);


const [loading,setLoading] = useState(true);

const [error,setError] = useState("");






// ===============================
// DATA LOADING
// ===============================


const loadDashboard = async()=>{


try{


setLoading(true);


const [
analyticsData,
healthData,
historyData

]= await Promise.all([

getAnalytics(),

getHealth(),

getPredictionHistory()

]);



setAnalytics(analyticsData);

setHealth(healthData);

setHistory(historyData);



setError("");



}
catch(err){


console.error(err);


setError(
"Unable to connect with SupportIQ backend"
);



}
finally{


setLoading(false);


}



};






useEffect(()=>{


loadDashboard();


},[]);









// ===============================
// HELPERS
// ===============================



const formatConfidence=(value)=>{


if(
value===undefined ||
value===null
)
return 0;



return value <= 1

?

Math.round(value*100)

:

Math.round(value);



};






const categories =
analytics?.categories || [];



const sentiment =
analytics?.sentiment || [];




const models =
analytics?.models || [];



const alerts =
analytics?.alerts || [];






const categoryColors=[

"#3b82f6",
"#22c55e",
"#ef4444",
"#a855f7",
"#f59e0b"

];



const sentimentColors=[

"#22c55e",
"#94a3b8",
"#ef4444"

];






// ===============================
// KPI CARDS
// ===============================



const cards=[


{
title:"Total Tickets",
value:
analytics?.total_tickets ?? 0,
icon:Ticket,
desc:"Processed by AI engine"
},



{
title:"High Priority Tickets",
value:
analytics?.critical_tickets ?? 0,
icon:AlertTriangle,
desc:"High priority cases"
},



{
title:"Deployed Model Accuracy",
value:
`${analytics?.accuracy ?? 0}%`,
icon:Brain,
desc:"XGBoost support-queue routing accuracy"
},



{
title:"Avg Confidence",
value:
`${formatConfidence(
analytics?.average_confidence
)}%`,
icon:Target,
desc:"Prediction reliability"
}



];






// ===============================
// STATUS CARDS
// ===============================



const status=[


{

title:"AI Service",

value:

health?.status==="healthy"

?

"Operational"

:

"Offline",

icon:ShieldCheck,

color:

health?.status==="healthy"

?

"text-green-400"

:

"text-red-400"

},



{


title:"Models",

value:

health?.models==="loaded"

?

"Ready"

:

"Loading",

icon:Cpu,

color:"text-blue-400"


},



{

title:"Latency",

value:

health?.latency

?

`${health.latency}ms`

:

"N/A",

icon:Clock,

color:"text-purple-400"


}



];






if(loading){


return (

<div className="
h-full
flex
items-center
justify-center
text-slate-400
">


Loading SupportIQ Intelligence Dashboard...


</div>


);


}





if(error){


return (

<div className="
h-full
flex
items-center
justify-center
text-red-400
">


{error}


</div>


);


}

return (

<div className="
min-h-screen
bg-slate-950
text-white
p-6
space-y-8
">





{/* ===========================
HEADER
=========================== */}



<div className="
flex
items-center
justify-between
">


<div>


<div className="
flex
items-center
gap-3
mb-2
">


<div className="
px-4
py-2
rounded-full
bg-blue-500/10
border
border-blue-400/20
text-blue-400
text-sm
flex
items-center
gap-2
">


<Activity size={16}/>


SupportIQ AI Monitoring


</div>


</div>




<h1 className="
text-4xl
font-bold
">

Enterprise NLP Dashboard

</h1>


<p className="
text-slate-400
mt-2
">

Real-time AI powered customer support intelligence.

</p>


</div>





<button


onClick={loadDashboard}


className="
flex
items-center
gap-2
px-5
py-3
rounded-xl
bg-blue-600
hover:bg-blue-500
transition
"


>


<RefreshCw size={18}/>

Refresh


</button>


</div>









{/* ===========================
KPI CARDS
=========================== */}



<div className="
grid
grid-cols-1
md:grid-cols-2
xl:grid-cols-4
gap-6
">


{

cards.map((card,index)=>{


const Icon = card.icon;


return (

<motion.div


key={card.title}


initial={{
opacity:0,
y:20
}}


animate={{
opacity:1,
y:0
}}


transition={{
delay:index*0.1
}}



className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-6
hover:border-blue-400/30
transition
"



>


<div className="
flex
justify-between
items-center
">


<div className="
p-3
rounded-xl
bg-blue-500/10
text-blue-400
">


<Icon size={26}/>


</div>


</div>




<h2 className="
text-4xl
font-bold
mt-6
">


{card.value}


</h2>



<p className="
text-white
font-semibold
mt-2
">


{card.title}


</p>


<p className="
text-sm
text-slate-400
mt-2
">


{card.desc}


</p>



</motion.div>


)


})


}


</div>









{/* ===========================
Top Support Queue
=========================== */}



<div className="
rounded-2xl
p-8
bg-gradient-to-r
from-blue-900/30
to-purple-900/30
border
border-white/10
">


<div className="
flex
items-center
gap-3
">


<TrendingUp
className="text-blue-400"
/>


<h2 className="
text-xl
font-bold
">


Most Common Support Queue


</h2>


</div>





<p className="
text-4xl
font-bold
text-blue-400
mt-5
">


{
analytics?.top_category
||
"No data"
}


</p>



<p className="
text-slate-400
mt-2
">


Most frequently predicted support queue


</p>



</div>









{/* ===========================
CHART SECTION
=========================== */}



<div className="
grid
grid-cols-1
xl:grid-cols-2
gap-6
">






{/* CATEGORY CHART */}



<div className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-6
">


<h2 className="
text-xl
font-bold
mb-6
flex
items-center
gap-3
">


<Ticket
className="text-blue-400"
/>


Ticket Categories


</h2>





<div className="
h-[320px]
">


{

categories.length > 0

?

<ResponsiveContainer>


<PieChart>


<Pie


data={categories}


dataKey="value"


nameKey="name"


cx="50%"

cy="50%"

outerRadius={110}



>


{

categories.map(
(entry,index)=>(


<Cell

key={index}

fill={
categoryColors[index %
categoryColors.length]
}

/>


)

)

}



</Pie>


<Tooltip/>


</PieChart>


</ResponsiveContainer>


:

<div className="
h-full
flex
items-center
justify-center
text-slate-500
">


No category data


</div>


}



</div>


</div>










{/* SENTIMENT CHART */}



<div className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-6
">


<h2 className="
text-xl
font-bold
mb-6
flex
items-center
gap-3
">


<Activity
className="text-green-400"
/>


Customer Sentiment


</h2>





<div className="
h-[320px]
">


{

sentiment.length > 0

?


<ResponsiveContainer>


<PieChart>


<Pie


data={sentiment}


dataKey="value"


nameKey="name"


cx="50%"

cy="50%"

outerRadius={110}



>


{

sentiment.map(
(entry,index)=>(


<Cell

key={index}

fill={
sentimentColors[index %
sentimentColors.length]
}

/>


)

)

}



</Pie>


<Tooltip/>


</PieChart>


</ResponsiveContainer>


:

<div className="
h-full
flex
items-center
justify-center
text-slate-500
">


No sentiment data


</div>


}


</div>


</div>



</div>








{/* ===========================
MODEL PERFORMANCE
=========================== */}



<div className="
rounded-2xl
bg-gradient-to-r
from-indigo-900/30
to-purple-900/30
border
border-white/10
p-8
">


<h2 className="
text-2xl
font-bold
flex
items-center
gap-3
mb-8
">


<Cpu
className="text-blue-400"
/>


AI Model Performance


</h2>





<div className="
grid
grid-cols-1
md:grid-cols-2
gap-6
">


{


models.map((model)=>(


<div

key={model.name}

className="
rounded-xl
bg-slate-950/60
border
border-white/10
p-5
"


>


<h3 className="
font-semibold
text-lg
">


{model.name}


</h3>



<p className="
text-slate-400
text-sm
mt-2
">


{model.task}


</p>



<div className="
mt-5
flex
justify-between
">


<span
className="
text-blue-400
font-bold
"
>


{model.accuracy}%


</span>


<span className="
text-slate-400
text-sm
">


Accuracy


</span>


</div>



</div>


))


}


</div>



</div>

{/* ===========================
RECENT AI DECISIONS
=========================== */}



<div className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-8
">


<div className="
flex
items-center
justify-between
mb-8
">


<div className="
flex
items-center
gap-3
">


<Activity
className="text-blue-400"
/>


<h2 className="
text-2xl
font-bold
">

Recent AI Decisions

</h2>


</div>



<div className="
text-sm
text-slate-400
">

Live Predictions

</div>


</div>







{

alerts.length > 0

?


<div className="
grid
grid-cols-1
md:grid-cols-2
xl:grid-cols-3
gap-6
">


{


alerts.map((item,index)=>(


<motion.div


key={index}


whileHover={{
y:-5
}}



className="
rounded-xl
bg-slate-950/70
border
border-white/10
p-5
"


>


<div className="
flex
justify-between
items-center
">


<h3 className="
font-bold
text-blue-400
">


{item.category}


</h3>



<span className="
text-xs
px-3
py-1
rounded-full
bg-red-500/10
text-red-400
">


{
item.priority || "Normal"
}


</span>


</div>





<div className="
mt-5
space-y-3
text-sm
">


<p>

<span className="
text-slate-400
">

Sentiment:

</span>

{" "}

{item.sentiment || "Unknown"}


</p>




<p>

<span className="
text-slate-400
">

Confidence:

</span>

{" "}

<span className="
text-green-400
font-semibold
">

{
formatConfidence(
item.confidence
)
}%

</span>


</p>




<p className="
text-xs
text-slate-500
">


{item.timestamp}


</p>



</div>



</motion.div>


))


}


</div>


:

<div className="
text-slate-500
text-center
py-10
">


No recent AI decisions available


</div>


}



</div>









{/* ===========================
PREDICTION HISTORY
=========================== */}



<div className="
rounded-2xl
bg-slate-900/70
border
border-white/10
p-8
">


<div className="
flex
items-center
justify-between
mb-8
">


<div className="
flex
items-center
gap-3
">


<Clock
className="text-blue-400"
/>


<h2 className="
text-2xl
font-bold
">

Prediction History

</h2>


</div>




<button

className="
flex
items-center
gap-2
px-4
py-2
rounded-xl
bg-blue-600
hover:bg-blue-500
transition
text-sm
"

>


<Download size={16}/>

Export


</button>



</div>









<div className="
overflow-x-auto
">


<table className="
w-full
">


<thead>


<tr className="
text-slate-400
border-b
border-white/10
">


<th className="
text-left
p-4
">

Support Queue

</th>


<th>

Priority

</th>


<th>

Sentiment

</th>


<th>

Confidence

</th>


</tr>


</thead>





<tbody>


{


history.slice(0,10).map(

(item,index)=>(


<tr

key={index}

className="
border-b
border-white/10
hover:bg-white/5
transition
"


>


<td className="
p-4
font-medium
">

{item.category || "Unknown"}

</td>




<td>


<span className="
px-3
py-1
rounded-full
bg-red-500/10
text-red-400
text-xs
">


{
item.priority || "Normal"
}


</span>


</td>





<td>


{item.sentiment || "Unknown"}


</td>





<td className="
text-green-400
font-semibold
">


{
formatConfidence(
item.confidence
)
}%

</td>





</tr>


)


)


}



</tbody>


</table>



</div>


</div>









{/* ===========================
AI SUMMARY
=========================== */}



<div className="
rounded-2xl
bg-gradient-to-r
from-blue-500/10
to-purple-500/10
border
border-white/10
p-8
">


<div className="
flex
items-center
gap-3
mb-8
">


<Brain
className="text-purple-400"
/>


<h2 className="
text-2xl
font-bold
">

AI Intelligence Summary

</h2>


</div>







<div className="
grid
md:grid-cols-3
gap-6
">


<div className="
bg-black/20
rounded-xl
p-5
">


<p className="
text-slate-400
text-sm
">

Top Support Queue

</p>


<h3 className="
text-xl
font-bold
mt-3
">

{
analytics?.top_category || "N/A"
}

</h3>


</div>







<div className="
bg-black/20
rounded-xl
p-5
">


<p className="
text-slate-400
text-sm
">

Predictions Generated

</p>


<h3 className="
text-xl
font-bold
mt-3
">

{
history.length
}

</h3>


</div>







<div className="
bg-black/20
rounded-xl
p-5
">


<p className="
text-slate-400
text-sm
">

Active Pipeline

</p>


<h3 className="
text-xl
font-bold
mt-3
">

TF-IDF + XGBoost

</h3>


</div>



</div>



</div>





</div>



);


}



export default Dashboard;