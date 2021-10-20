import Layout from "./Layout";
import Home from "./Home";
import About from "./About";
import Evaluate from "./Evaluate";
import Contact from "./Contact";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

function App() {
  return (
  <Layout>
    <Router>
      <div className="App">
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/about">
              <About />
            </Route>
            <Route exact path="/evaluate">
              <Evaluate />
            </Route>
            <Route exach path="/contact">
              <Contact />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
    </Layout>
  );
}

export default App;
