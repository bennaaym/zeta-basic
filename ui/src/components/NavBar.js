import {Link} from 'react-router-dom'
const NavBar = ({items,theme}) => {
    return (
        <>
            <nav className= {` border-b border-${theme.borderColor}	p-5 bg-${theme.navBgColor}`}>
                <div className = "flex flex-row justify-between items-center ">
                    <h1 className ={`text-${theme.text} text-xl font-semibold tracking-wide`}>&#950; basic editor</h1>
                    <ul className ={`flex flex-row text-${theme.text} text-md font-medium uppercase`}>
                        {
                            items.map((item,index) =>{
                                return (
                                    <Link key ={index} to={item.url}>
                                        {item.name && <li className = "ml-5">{item.name}</li>}
                                    </Link>
                                )
                            })
                        }   
                    </ul>
                </div>
            </nav>
        </>
    );
}
 
export default NavBar;