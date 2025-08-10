import { useState } from 'react';
import { EXAMPLES } from '../data';
import TabButton from './TabButton.jsx';
import Section from './Section.jsx';
import Tab  from './Tab.jsx';

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
        <Section id="examples" title="Examples">
          <Tab
          // buttonElement="menu"
          // very important to use built in element in side the "" as string but for 
          // custom element we have to use the curly braces {} to pass for example 
          // instead of "menu" we can do {Section} but for ul, div or li we have to pass it as 
          // "ul", "div" or "li"
          buttons={
            <>
              <TabButton isSelected={selectedTopic==="components"} onSelect={()=>handleTabSelect("components")}>Components</TabButton>
              <TabButton isSelected={selectedTopic==='jsx'} onSelect={()=>handleTabSelect("jsx")}>JSX</TabButton>
              <TabButton isSelected={selectedTopic==='props'} onSelect={()=>handleTabSelect("props")}>Props</TabButton>
              <TabButton isSelected={selectedTopic==='state'} onSelect={()=>handleTabSelect("state")}>State</TabButton>
            </>
          }>
            {tabContent}
          </Tab>

        </Section>
    );}