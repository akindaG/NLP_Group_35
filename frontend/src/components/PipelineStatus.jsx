import {
    Search,
    Brain,
    Cpu,
    Activity,
    CheckCircle
} from "lucide-react";


function PipelineStatus(){

const pipeline = [

{
title:"Text Processing",
model:"NLP Preprocessing",
icon:Search
},

{
title:"Ticket Classification",
model:"DistilBERT",
icon:Brain
},

{
title:"Priority Prediction",
model:"XGBoost",
icon:Cpu
},

{
title:"Sentiment Analysis",
model:"Transformer Model",
icon:Activity
}

];


return (

<div className="
bg-white/5
border
border-white/10
rounded-3xl
p-8
">


<div className="
flex
items-center
gap-3
mb-6
">

<Activity
className="text-yellow-400"
/>


<h2 className="
text-xl
font-semibold
">

AI Processing Pipeline

</h2>


</div>





<div className="
space-y-4
">


{
pipeline.map((item,index)=>{


const Icon=item.icon;


return (

<div

key={index}

className="
flex
items-center
justify-between
bg-slate-900/60
border
border-white/10
rounded-xl
p-4
"


>


<div className="
flex
items-center
gap-4
">


<div className="
w-10
h-10
rounded-xl
bg-blue-500/20
flex
items-center
justify-center
text-blue-400
">

<Icon size={20}/>

</div>



<div>

<h3 className="
font-semibold
">

{item.title}

</h3>


<p className="
text-xs
text-slate-400
">

{item.model}

</p>


</div>



</div>





<div className="
flex
items-center
gap-2
text-green-400
text-sm
">

<CheckCircle size={16}/>

Active


</div>



</div>


)


})

}


</div>


</div>


)

}


export default PipelineStatus;