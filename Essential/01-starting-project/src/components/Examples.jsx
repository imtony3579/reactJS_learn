import { useState } from 'react';
import { EXAMPLES } from '../data';
import TabButton from './TabButton.jsx';


export default function Examples() {
const [ selectedTopic, setSelectedTopic ] = 
  useState();


  function handleTabSelect(tabName) {
    setSelectedTopic(tabName);
  }

  let tabContent = <p>Select a topic to see the example code.</p>;

  if (selectedTopic) {
    tabContent = (
      <div id="tab-content">
        <h3>{EXAMPLES[selectedTopic].title}</h3>
        <p>{EXAMPLES[selectedTopic].description}</p>
        <pre>
          <code>
            {EXAMPLES[selectedTopic].code}
          </code>
        </pre>
      </div>
    );}
    return (
         <section id="examples">
          <h2>Examples</h2>
          <menu>
            <TabButton isSelected={selectedTopic==="components"} onSelect={()=>handleTabSelect("components")}>Components</TabButton>
            <TabButton isSelected={selectedTopic==='jsx'} onSelect={()=>handleTabSelect("jsx")}>JSX</TabButton>
            <TabButton isSelected={selectedTopic==='props'} onSelect={()=>handleTabSelect("props")}>Props</TabButton>
            <TabButton isSelected={selectedTopic==='state'} onSelect={()=>handleTabSelect("state")}>State</TabButton>
          </menu>
    
            {tabContent}
        </section>
    );}