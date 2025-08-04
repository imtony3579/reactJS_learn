import { CORE_CONCEPTS } from "./data";
import Header from "./components/Header/Header.jsx";
import CoreConcept from "./components/CoreConcept.jsx";
import TabButton from "./components/TabButton.jsx";  



function App() {
  
  let tabContent = "please click a button";


  function handleTabSelect(tabName) {
    tabContent = `Selected tab: ${tabName}`;
  }

  return (
    <div>
      <Header />
      <main>
        <section id='core-concepts'>
          <h2>Core Concepts</h2>
          <ul>
            <CoreConcept {...CORE_CONCEPTS[0]} />
            <CoreConcept {...CORE_CONCEPTS[1]} />
            <CoreConcept {...CORE_CONCEPTS[2]} />
            <CoreConcept title={CORE_CONCEPTS[3].title} 
            description={CORE_CONCEPTS[3].description}
            image={CORE_CONCEPTS[3].image} />

          </ul>
        </section>
        <section id="examples">
          <h2>Examples</h2>
          <menu>
            <TabButton onSelect={()=>handleTabSelect("Components")}>Components</TabButton>
            <TabButton onSelect={()=>handleTabSelect("JSX")}>JSX</TabButton>
            <TabButton onSelect={()=>handleTabSelect("Props")}>Props</TabButton>
            <TabButton onSelect={()=>handleTabSelect("State")}>State</TabButton>
          </menu>
          {tabContent && <p>{tabContent}</p>}
          </section>
    
      </main>
    </div>
  );
}

export default App;
