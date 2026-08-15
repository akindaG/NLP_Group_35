import {
CheckCircle,
AlertTriangle
} from "lucide-react";


function PredictionCard(){


return (

<div className="
bg-gradient-to-br
from-blue-500/10
to-purple-500/10
border
border-white/10
rounded-3xl
p-8
">


<div className="
flex
justify-between
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
md:grid-cols-2
gap-8
">


<div>

<p className="text-slate-400 text-sm">
Category
</p>

<h3 className="text-xl font-semibold">
Billing Issue
</h3>

</div>




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

High

</h3>

</div>




<div>

<p className="text-slate-400 text-sm">
Sentiment
</p>

<h3 className="text-xl font-semibold">
Negative
</h3>

</div>




<div>

<p className="text-slate-400 text-sm">
Routing
</p>

<h3 className="text-xl font-semibold">
Finance Support
</h3>

</div>



</div>



</div>


)

}


export default PredictionCard;