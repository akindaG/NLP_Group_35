import {
CheckCircle,
AlertTriangle,
Brain,
Building2,
Smile,
Cpu
} from "lucide-react";


function PredictionCard({data}){


if(!data)
return null;



return (

<div className="
bg-gradient-to-br
from-blue-500/10
to-purple-500/10
border
border-white/10
rounded-3xl
p-8
mt-10
">



<div className="
flex
justify-between
items-center
mb-8
">


<h2 className="
text-2xl
font-bold
">

AI Prediction Result

</h2>



<div className="
flex
gap-2
items-center
text-green-400
">

<CheckCircle size={18}/>

Completed

</div>


</div>





<div className="
grid
md:grid-cols-3
gap-6
">



{/* Category */}

<div>

<p className="text-slate-400 text-sm">
Category
</p>

<h3 className="
text-xl
font-semibold
flex
items-center
gap-2
">

<Brain size={18}
className="text-blue-400"
/>

{data.category}

</h3>


</div>





{/* Priority */}

<div>


<p className="text-slate-400 text-sm">
Priority
</p>


<h3 className="
text-xl
font-semibold
text-red-400
flex
items-center
gap-2
">

<AlertTriangle size={18}/>

{data.priority}


</h3>


</div>






{/* Sentiment */}

<div>


<p className="text-slate-400 text-sm">
Sentiment
</p>


<h3
className={`
text-xl font-semibold
${
data.sentiment === "Negative"
?
"text-red-400"
:
data.sentiment === "Positive"
?
"text-green-400"
:
"text-yellow-400"
}
`}
>

{data.sentiment}

</h3>


</div>






{/* Department */}

<div>


<p className="text-slate-400 text-sm">
Routing Department
</p>


<h3 className="
text-xl
font-semibold
flex
items-center
gap-2
">


<Building2
size={18}
className="text-purple-400"
/>


{data.department}


</h3>


</div>







{/* Model */}

<div>


<p className="text-slate-400 text-sm">
Model Used
</p>


<h3 className="
text-xl
font-semibold
flex
items-center
gap-2
">


<Cpu
size={18}
className="text-green-400"
/>


{data.model_used}


</h3>


</div>






{/* Confidence */}

<div>


<p className="text-slate-400 text-sm">
Confidence
</p>


<h3 className="text-xl font-semibold text-green-400">
{
(data.confidence * 100).toFixed(1)
}%

</h3>

<p className="text-xs text-slate-400 mt-1">

{
data.confidence > 0.7
?
"High confidence prediction"
:
data.confidence > 0.4
?
"Moderate confidence prediction"
:
"Low confidence prediction"

}

</p>

</div>




</div>








<div className="mt-8">


<p className="text-slate-400 text-sm">
Processed Text
</p>


<p className="
mt-2
text-slate-200
">

{data.cleaned_text}

</p>


</div>



</div>


)


}


export default PredictionCard;