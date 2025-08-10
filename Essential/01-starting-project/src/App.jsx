import { use, useState , Fragment} from "react";

import Header from "./components/Header/Header.jsx";
import Examples from "./components/Examples.jsx";
import CoreConcepts from "./components/CoreConcepts.jsx";



function App() {
  

  return (
    <>
      <Header />
      <main>
        <CoreConcepts /> 
        <Examples/> 

      </main>
    </>
  );
}

export default App;
