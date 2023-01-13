import React from 'react';
import Navbar from './Navbar';
import Pricing from './pages/Pricing';
import About from './pages/About';
import Home from './pages/Home';
import { Route, Routes } from 'react-router-dom';
//import TodoList from './TodoList';
//import { v4 as uuidv4 } from 'uuid';

//const localkey = 'todoApp.todos'
// Idk, need to push

function App() {

  return(
    <>
    <Navbar />
    <div className='container'>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/pricing" element={<Pricing />}/>
        <Route path="/about" element={<About />}/>
      </Routes>
    </div>
    </>
  )
  /*
  const [todos, setTodos] = useState([])
  const nameRef = useRef()

  useEffect(() => {
    const storedTodos = JSON.parse(localStorage.getItem(localkey))
    if (storedTodos) setTodos( prevTodos => [...prevTodos, ...storedTodos] );
  }, [])

  useEffect(() => {
    localStorage.setItem(localkey, JSON.stringify(todos))
  }, [todos])

  function clearTodo(){
    const newTodos = todos.filter(todo => !todo.complete)
    setTodos(newTodos)
  }

  function toggleTodo(id){
    const newList = [...todos]
    const todoo = newList.find(todos => todoo.id === id)
    todoo.complete = !todoo.complete
    setTodos(newList)
  }

  function handleAddTodo(e) {
    const name = nameRef.current.value
    if (name === '') return
    setTodos(prevTodos => {
      return [...prevTodos, {id: uuidv4(), name: name, complete: false}]
    })
    nameRef.current.value = null
  }

  return (
  <>
    <TodoList todos={todos} toggleTodo={toggleTodo}/>
    <input ref={ nameRef } type="text"/>
    <button onClick={handleAddTodo}>Add ToDo</button>
    <button onClick={clearTodo}>Clear completed ToDos</button>
    <div>{todos.filter(todo => !todo.complete).length} left to do</div>
    </>
    )*/
}

export default App;
