import {Switch , Route} from 'react-router-dom'
import Home from './components/home/Home'
import Guide from './components/guide/Guide'
import NavBar from './components/NavBar'
import './assets/css/global.css'
import ThemeContextProvider from './context/ThemeContext'
import {ThemeContext} from './context/ThemeContext'
import CodeContextProvide from './context/CodeContext'

const App = () => {

  return (   
    <ThemeContextProvider>
        <ThemeContext.Consumer>{(context) => {

          const {theme} = context
          const activeTheme = theme.isLight ? theme.light : theme.dark

          return(
            <div className = 'App min-h-screen'>
                <NavBar items={[
                    {name : 'home', url : '/'},
                    {name : 'guide', url:'/guide'},
                  ]}
                    
                    theme = {activeTheme}
                    />

                <Switch>
                  <CodeContextProvide>
                    <Route exact path='/' component={Home}/>
                    <Route path='/guide'>
                      <Guide theme = {activeTheme}/>
                    </Route>

                  </CodeContextProvide>
                </Switch>

            </div>
          )
        }}

    </ThemeContext.Consumer>

</ThemeContextProvider>

    
  );
}

export default App;
