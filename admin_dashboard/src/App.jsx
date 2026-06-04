import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {getJSON, postJSON} from './api';
import './style.css';
function App(){
  const [summary,setSummary]=useState(null); const [leads,setLeads]=useState([]); const [signals,setSignals]=useState([]);
  async function load(){ setSummary(await getJSON('/analytics/summary')); setLeads(await getJSON('/leads/')); setSignals(await getJSON('/market/signals/top')); }
  async function hunt(){ await postJSON('/leads/hunt',{query:'AI software automation outsourcing',region:'USA',limit_per_source:5}); await load(); }
  useEffect(()=>{load()},[]);
  return <div className="app"><h1>AI Growth Infrastructure</h1><button onClick={hunt}>Run Lead Hunter</button><section><h2>Pipeline</h2><pre>{JSON.stringify(summary,null,2)}</pre></section><section><h2>Leads</h2>{leads.map(l=><div className="card" key={l.id}><b>#{l.id} | {l.score}</b><br/>{l.title}<br/><small>{l.status} | {l.region}</small></div>)}</section><section><h2>Market Signals</h2>{signals.map(s=><div className="card" key={s.id}><b>{s.opportunity_score}</b> {s.title}<br/><small>{s.region} | {s.niche}</small></div>)}</section></div>
}
createRoot(document.getElementById('root')).render(<App/>);
