"""Additional top React interview questions — expands react section to 50+."""

from data.interview_content import InterviewItem

MARKET_ITEMS: dict[tuple[str, str], list[InterviewItem]] = {
    ("react", "foundation"): [
        InterviewItem(
            "react-jsx-basics",
            "What is JSX and how does it differ from HTML?",
            "JSX is a syntax extension that compiles to React.createElement calls.",
            "",
        ),
        InterviewItem(
            "react-functional-components",
            "Why did React move toward functional components over class components?",
            "Hooks give function components state and lifecycle without classes.",
            "",
        ),
        InterviewItem(
            "react-props-state",
            "What is the difference between props and state in React?",
            "Props are read-only inputs from parent; state is local mutable data.",
            "",
        ),
        InterviewItem(
            "react-usestate",
            "How does the useState hook work?",
            "Returns a state value and setter; updates schedule a re-render.",
            "",
        ),
        InterviewItem(
            "react-conditional-rendering",
            "What are common patterns for conditional rendering in React?",
            "Use &&, ternary, or early return — never conditionally call hooks.",
            "",
        ),
        InterviewItem(
            "react-lists-keys",
            "Why are keys important when rendering lists in React?",
            "Stable keys help reconciliation match items across renders.",
            "",
        ),
        InterviewItem(
            "react-virtual-dom",
            "What is the Virtual DOM and why does React use it?",
            "In-memory tree diffed against real DOM for efficient updates.",
            "",
        ),
        InterviewItem(
            "react-reconciliation",
            "How does React reconciliation decide what to update?",
            "Compares element type and key; reuses DOM when possible.",
            "",
        ),
        InterviewItem(
            "react-event-handling",
            "How does event handling work in React?",
            "Synthetic events wrap native events; pass functions, not invoke them.",
            "",
        ),
        InterviewItem(
            "react-controlled-forms",
            "What are controlled vs uncontrolled form components?",
            "Controlled: React state is source of truth; uncontrolled: refs read DOM.",
            "",
        ),
        InterviewItem(
            "react-useeffect",
            "What does useEffect do and when does it run?",
            "Runs side effects after render; dependency array controls re-runs.",
            "",
        ),
        InterviewItem(
            "react-lifting-state",
            "What is lifting state up and when should you use it?",
            "Move shared state to the closest common ancestor component.",
            "",
        ),
        InterviewItem(
            "react-children-composition",
            "How does component composition work with the children prop?",
            "Pass JSX as children to build flexible wrapper components.",
            "",
        ),
        InterviewItem(
            "react-fragments",
            "What are React Fragments and why use them?",
            "Group elements without adding extra DOM nodes.",
            "",
        ),
        InterviewItem(
            "react-styling",
            "What are common approaches to styling React components?",
            "CSS Modules, Tailwind, CSS-in-JS, or plain className strings.",
            "",
        ),
        InterviewItem(
            "react-strict-mode",
            "What does React StrictMode do in development?",
            "Double-invokes effects and warns about unsafe legacy patterns.",
            "",
        ),
        InterviewItem(
            "react-element-rendering",
            "How does React.createElement relate to JSX?",
            "Babel/TS compiles JSX into createElement(type, props, ...children).",
            "",
        ),
        InterviewItem(
            "react-one-way-data-flow",
            "Explain one-way data flow in React.",
            "Data flows down via props; events flow up via callbacks.",
            "",
        ),
    ],
    ("react", "intermediate"): [
        InterviewItem(
            "react-usecontext",
            "How does useContext work and when should you use it?",
            "Subscribe to nearest Provider value; good for theme, auth, locale.",
            "",
        ),
        InterviewItem(
            "react-usereducer",
            "When do you choose useReducer over useState?",
            "Complex state transitions, multiple sub-values, or predictable updates.",
            "",
        ),
        InterviewItem(
            "react-useref",
            "What are common use cases for useRef?",
            "DOM access, storing mutable values without re-renders, previous value.",
            "",
        ),
        InterviewItem(
            "react-usememo",
            "What does useMemo memoize and when is it worth using?",
            "Caches expensive computed values between renders when deps unchanged.",
            "",
        ),
        InterviewItem(
            "react-usecallback",
            "What is useCallback and how does it differ from useMemo?",
            "Returns stable function reference; prevents child re-renders with memo.",
            "",
        ),
        InterviewItem(
            "react-custom-hooks",
            "How do you build and test custom hooks?",
            "Extract reusable stateful logic; prefix with use; test via renderHook.",
            "",
        ),
        InterviewItem(
            "react-useeffect-advanced",
            "What are common useEffect pitfalls and cleanup patterns?",
            "Missing deps, stale closures, and forgetting to abort fetch/subscriptions.",
            "",
        ),
        InterviewItem(
            "react-router",
            "How does React Router v6+ handle routing?",
            "Declarative Routes with element prop; nested routes via Outlet.",
            "",
        ),
        InterviewItem(
            "react-router-data",
            "What are loaders, actions, and protected routes in React Router?",
            "Data APIs fetch before render; loaders/actions replace many useEffect fetches.",
            "",
        ),
        InterviewItem(
            "react-redux-toolkit",
            "How does Redux Toolkit simplify Redux in React apps?",
            "createSlice, configureStore, RTK Query — less boilerplate than classic Redux.",
            "",
        ),
        InterviewItem(
            "react-zustand",
            "When would you pick Zustand over Redux?",
            "Minimal boilerplate, hook-based store, great for small-to-medium apps.",
            "",
        ),
        InterviewItem(
            "react-tanstack-query",
            "What problems does TanStack Query (React Query) solve?",
            "Server state caching, background refetch, deduplication, stale-while-revalidate.",
            "",
        ),
        InterviewItem(
            "react-error-boundaries",
            "What are error boundaries and what can they not catch?",
            "Class or library boundaries catch render errors; not event/async errors.",
            "",
        ),
        InterviewItem(
            "react-portals",
            "What are React portals and common use cases?",
            "Render children into a DOM node outside parent hierarchy — modals, tooltips.",
            "",
        ),
        InterviewItem(
            "react-forwardref",
            "Why use forwardRef in React components?",
            "Expose DOM or imperative handle to parent while keeping encapsulation.",
            "",
        ),
        InterviewItem(
            "react-memo-optimization",
            "When should you use React.memo?",
            "When a component re-renders often with the same props — profile first.",
            "",
        ),
        InterviewItem(
            "react-form-validation",
            "How do you implement form validation in React?",
            "Controlled fields plus schema libs (Zod/Yup) or React Hook Form.",
            "",
        ),
        InterviewItem(
            "react-testing-rtl",
            "What is React Testing Library and its testing philosophy?",
            "Test behavior from user perspective — queries by role/label, not implementation.",
            "",
        ),
        InterviewItem(
            "react-typescript",
            "How do you type React components, props, and events in TypeScript?",
            "FC or explicit props interface; React.ChangeEvent, ComponentPropsWithoutRef.",
            "",
        ),
        InterviewItem(
            "react-context-patterns",
            "What are best practices for React Context to avoid performance issues?",
            "Split contexts, memoize value, combine with useMemo — avoid huge single context.",
            "",
        ),
        InterviewItem(
            "react-suspense-data",
            "How does Suspense work with data fetching libraries?",
            "Throw promise during render; Suspense boundary shows fallback until resolved.",
            "",
        ),
    ],
    ("react", "advanced"): [
        InterviewItem(
            "react-lazy-code-splitting",
            "How do React.lazy and dynamic import enable code splitting?",
            "lazy() loads component on demand; wrap with Suspense for loading UI.",
            "",
        ),
        InterviewItem(
            "react-performance",
            "What are proven React performance optimization techniques?",
            "Virtualize lists, split code, memoize wisely, defer non-urgent updates.",
            "",
        ),
        InterviewItem(
            "react-use-transition",
            "What is useTransition and how does concurrent rendering help UX?",
            "Mark updates non-urgent; React keeps UI responsive during heavy renders.",
            "",
        ),
        InterviewItem(
            "react-ssr-nextjs",
            "Compare CSR, SSR, SSG, and ISR in Next.js.",
            "SSR per request, SSG at build, ISR revalidates static pages on interval.",
            "",
        ),
        InterviewItem(
            "react-server-components",
            "What are React Server Components (RSC)?",
            "Server-only components — zero client bundle; fetch DB directly, stream HTML.",
            "",
        ),
        InterviewItem(
            "react-18-concurrent",
            "What concurrent features shipped in React 18?",
            "Automatic batching, transitions, Suspense improvements, streaming SSR.",
            "",
        ),
        InterviewItem(
            "react-19-features",
            "What are notable React 19 features for interviews?",
            "Actions, useActionState, useOptimistic, ref as prop, document metadata.",
            "",
        ),
        InterviewItem(
            "react-security-xss",
            "How does React help prevent XSS and where are you still vulnerable?",
            "Escapes JSX by default; danger with dangerouslySetInnerHTML and raw HTML APIs.",
            "",
        ),
        InterviewItem(
            "react-micro-frontends",
            "How do micro-frontends work with React (Module Federation)?",
            "Independent deployable apps share runtime via webpack Module Federation or single-spa.",
            "",
        ),
        InterviewItem(
            "react-hydration",
            "What is hydration and how do you fix hydration mismatches?",
            "Client attaches listeners to server HTML; mismatch when server/client differ.",
            "",
        ),
        InterviewItem(
            "react-compiler-optimization",
            "What is the React Compiler and how does it change memoization?",
            "Compile-time auto-memoization reduces manual useMemo/useCallback boilerplate.",
            "",
        ),
    ],
}

MARKET_DETAILED: dict[str, dict] = {
    "react-jsx-basics": {
        "explanation": (
            "**JSX (JavaScript XML)** lets you write UI that looks like HTML inside JavaScript. "
            "It is **not** parsed by the browser — Babel/TypeScript compiles it to **`React.createElement`** "
            "calls that describe a virtual element tree. JSX rules differ from HTML: **`className`** instead of "
            "`class`, **`htmlFor`** instead of `for`, and you must **wrap multiple siblings** in a parent or Fragment. "
            "Expressions go inside **`{curly braces}`**."
        ),
        "code": """import { createElement } from 'react';

// JSX compiles to createElement
const element = <h1 className="title">Hello, {user.name}</h1>;
// Equivalent:
const same = createElement('h1', { className: 'title' }, 'Hello, ', user.name);

function Greeting({ name }: { name: string }) {
  return (
    <>
      <p>Welcome back</p>
      <strong>{name.toUpperCase()}</strong>
    </>
  );
}""",
        "language": "typescript",
        "key_points": [
            "JSX compiles to React.createElement — not native HTML",
            "Use className, htmlFor, camelCase DOM properties",
            "Embed JavaScript expressions with { }",
            "Must return a single root (Fragment <> ok)",
        ],
    },
    "react-functional-components": {
        "explanation": (
            "**Functional components** are plain functions that accept props and return JSX. Since **React 16.8 Hooks**, "
            "they support state, effects, context, and refs — everything class components offered, with less boilerplate. "
            "React team recommends functions for new code; **class components** remain in legacy codebases. "
            "Hooks rules (only at top level, only in React functions) apply exclusively to function components."
        ),
        "code": """// Modern functional component with hooks
import { useState } from 'react';

type CounterProps = { initial?: number };

export function Counter({ initial = 0 }: CounterProps) {
  const [count, setCount] = useState(initial);
  return (
    <button onClick={() => setCount((c) => c + 1)}>
      Count: {count}
    </button>
  );
}

// Class equivalent (legacy — know for interviews)
// class Counter extends React.Component { state = { count: 0 }; render() { ... } }""",
        "language": "typescript",
        "key_points": [
            "Functions + hooks replaced most class use cases",
            "Less boilerplate — no this binding, no lifecycle method names",
            "Custom hooks only work in function components",
            "Still know class components for maintenance interviews",
        ],
    },
    "react-props-state": {
        "explanation": (
            "**Props** are **read-only inputs** passed from parent to child — the child must never mutate them. "
            "**State** is **local, mutable data** owned by a component; updating state triggers a re-render. "
            "When multiple components need the same data, **lift state up** to their closest common ancestor. "
            "Props flow down; events/callbacks flow up — this is React's **one-way data flow**."
        ),
        "code": """function Parent() {
  const [filter, setFilter] = useState('all');

  return (
    <div>
      <FilterBar value={filter} onChange={setFilter} />  {/* props down */}
      <TodoList filter={filter} />
    </div>
  );
}

function FilterBar({
  value,
  onChange,
}: {
  value: string;
  onChange: (v: string) => void;
}) {
  // ❌ value = 'done' — never mutate props
  return (
    <select value={value} onChange={(e) => onChange(e.target.value)}>
      <option value="all">All</option>
      <option value="done">Done</option>
    </select>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Props = read-only; state = owned and mutable",
            "setState schedules re-render; direct mutation does not",
            "Lift shared state to common parent",
            "Callbacks pass events up the tree",
        ],
    },
    "react-usestate": {
        "explanation": (
            "**`useState(initialValue)`** returns `[value, setValue]`. The initial value is used only on **first render**; "
            "pass a **function** (`useState(() => expensive())`) for lazy initialization. Updates may be **batched** "
            "in React 18+. Use the **functional updater** `setCount(c => c + 1)` when the new state depends on "
            "the previous state to avoid stale closures."
        ),
        "code": """import { useState } from 'react';

function SignupForm() {
  const [email, setEmail] = useState('');
  const [items, setItems] = useState<string[]>([]);

  const addItem = (item: string) => {
    // Functional update — safe when depending on previous state
    setItems((prev) => [...prev, item]);
  };

  return (
    <form onSubmit={(e) => { e.preventDefault(); addItem(email); setEmail(''); }}>
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <ul>{items.map((i) => <li key={i}>{i}</li>)}</ul>
    </form>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Returns [state, setter] tuple",
            "Lazy init: useState(() => computeInitial())",
            "Functional updater avoids stale state in closures",
            "React 18 batches multiple setStates in same event",
        ],
    },
    "react-conditional-rendering": {
        "explanation": (
            "React renders **JavaScript expressions** in JSX, so you can use **`&&`**, **ternaries**, or "
            "**early return** for conditional UI. **`{count && <Badge />}`** works but beware **`{count && <List />}`** "
            "when count is `0` — it renders `0`. Prefer **`count > 0 &&`** or explicit ternary. "
            "**Never** conditionally call hooks — hooks must run in the same order every render."
        ),
        "code": """function OrderStatus({ status, items }: { status: string; items: number }) {
  if (status === 'loading') return <Spinner />;

  return (
    <div>
      {status === 'error' ? (
        <Alert type="error">Something went wrong</Alert>
      ) : (
        <>
          {items > 0 && <p>{items} items in cart</p>}
          {items === 0 ? <EmptyCart /> : <CartSummary count={items} />}
        </>
      )}
    </div>
  );
}""",
        "language": "typescript",
        "key_points": [
            "&&, ternary, early return — all valid",
            "Watch falsy numbers: 0 && <X /> renders 0",
            "Never wrap hooks in if/for — Rules of Hooks",
            "Extract sub-components for complex branches",
        ],
    },
    "react-lists-keys": {
        "explanation": (
            "When rendering arrays, each child needs a **stable, unique `key`** prop so React's reconciler can "
            "match items across renders. **Index as key** breaks when list is reordered, filtered, or items inserted — "
            "causing wrong component state and poor performance. Use **database IDs** or other stable identifiers. "
            "Keys are **not passed as props** to the component — React uses them internally."
        ),
        "code": """function TodoList({ todos }: { todos: { id: string; text: string; done: boolean }[] }) {
  return (
    <ul>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}          // ✅ stable id from server
          todo={todo}
        />
      ))}
    </ul>
  );
}

// ❌ Avoid index keys when list mutates:
// todos.map((todo, index) => <TodoItem key={index} ... />)""",
        "language": "typescript",
        "key_points": [
            "Keys help reconciliation identify which items changed",
            "Use stable unique ids — not random per render",
            "Index keys fail on reorder/delete/insert",
            "Keys are not accessible inside child via props",
        ],
    },
    "react-virtual-dom": {
        "explanation": (
            "The **Virtual DOM** is a lightweight **JavaScript representation** of the UI tree. On state change, "
            "React builds a **new virtual tree**, **diffs** it against the previous one, and applies the **minimal set "
            "of DOM mutations** (the \"patch\"). This batches updates and avoids expensive direct DOM manipulation. "
            "It is an implementation detail — you still optimize with keys, memoization, and avoiding unnecessary renders."
        ),
        "code": """// Conceptual — React does this internally
function App() {
  const [count, setCount] = useState(0);

  // State change → new VDOM tree → diff → patch real DOM
  return (
    <main>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </main>
  );
}

// Fiber architecture (React 16+) enables incremental rendering
// and priority-based updates for concurrent features""",
        "language": "typescript",
        "key_points": [
            "VDOM = in-memory JS tree, not a second real DOM",
            "Diff + patch minimizes actual DOM operations",
            "Fiber enables interruptible/concurrent rendering",
            "Profile real bottlenecks — VDOM is not magic",
        ],
    },
    "react-reconciliation": {
        "explanation": (
            "**Reconciliation** is React's algorithm for comparing the new element tree with the previous one. "
            "If **element type differs** (e.g., `<div>` → `<span>`), React **unmounts** the old subtree and mounts new. "
            "If type is same, React **updates props** and recurses on children. **`key`** at the same level tells React "
            "which list items correspond across renders. Understanding this explains why **component identity** and **keys** matter."
        ),
        "code": """// Same type → update props, keep DOM node where possible
function Toggle({ on }: { on: boolean }) {
  return on ? <StatusBadge label="Active" color="green" /> : <StatusBadge label="Off" color="gray" />;
}

// Different type → full remount (state reset)
function SwitchMode({ edit }: { edit: boolean }) {
  return edit ? <EditorForm /> : <ReadOnlyView />;  // switching remounts
}

// Keys force remount when identity must reset
function UserPanel({ userId }: { userId: string }) {
  return <Profile key={userId} userId={userId} />;  // fresh state per user
}""",
        "language": "typescript",
        "key_points": [
            "Different element type → unmount + mount",
            "Same type → update props in place",
            "Keys identify list siblings across renders",
            "key on component resets internal state",
        ],
    },
    "react-event-handling": {
        "explanation": (
            "React wraps native events in **SyntheticEvents** for cross-browser consistency and **event pooling** "
            "(legacy). Pass **function references** to handlers: `onClick={handleClick}` not `onClick={handleClick()}`. "
            "React 17+ attaches listeners to the **root container**, not document. Use "
            "**`e.preventDefault()`** and **`e.stopPropagation()`** like native events."
        ),
        "code": """function SearchForm({ onSearch }: { onSearch: (q: string) => void }) {
  const [query, setQuery] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch(query.trim());
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={query}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => setQuery(e.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Pass function reference — not invoked result",
            "SyntheticEvent wraps native event",
            "Type events: React.ChangeEvent, FormEvent, MouseEvent",
            "preventDefault for forms; stopPropagation to bubble control",
        ],
    },
    "react-controlled-forms": {
        "explanation": (
            "**Controlled components** bind input **`value`** to React **state** — React is the single source of truth. "
            "**Uncontrolled components** store values in the **DOM**; you read them via **`ref`** on submit. "
            "Controlled inputs enable **live validation**, **formatting**, and **conditional disable**. "
            "Libraries like **React Hook Form** blend both — refs internally with minimal re-renders."
        ),
        "code": """function ControlledLogin() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <form onSubmit={(e) => { e.preventDefault(); login(email, password); }}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button disabled={!email || password.length < 8}>Sign in</button>
    </form>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Controlled = value + onChange tied to state",
            "Uncontrolled = ref.current.value on submit",
            "Controlled enables instant validation UX",
            "React Hook Form reduces controlled re-render cost",
        ],
    },
    "react-useeffect": {
        "explanation": (
            "**`useEffect(fn, deps)`** runs **after paint** (by default) for side effects: fetch, subscriptions, DOM sync. "
            "Omitting **`deps`** runs every render; **`[]`** runs once on mount. Return a **cleanup function** for "
            "timers, listeners, and abort controllers. **`useLayoutEffect`** runs synchronously after DOM mutations — "
            "use for measuring layout before paint."
        ),
        "code": """function UserProfile({ userId }: { userId: string }) {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    fetch(`/api/users/${userId}`, { signal: controller.signal })
      .then((r) => r.json())
      .then(setUser)
      .catch((err) => {
        if (err.name !== 'AbortError') console.error(err);
      });

    return () => controller.abort();  // cleanup on userId change or unmount
  }, [userId]);

  if (!user) return <Spinner />;
  return <h1>{user.name}</h1>;
}""",
        "language": "typescript",
        "key_points": [
            "Runs after render — not during render",
            "Deps array controls when effect re-runs",
            "Always cleanup subscriptions and fetches",
            "Prefer React Query over raw useEffect fetch",
        ],
    },
    "react-lifting-state": {
        "explanation": (
            "When **sibling components** need to share data, move the shared **state up** to their **closest common "
            "parent** and pass it down as props along with **setter callbacks**. This keeps a **single source of truth** "
            "and preserves one-way data flow. For deeply nested trees, consider **Context**, **composition**, or "
            "a **state library** instead of excessive prop drilling."
        ),
        "code": """function TemperatureApp() {
  const [celsius, setCelsius] = useState(0);

  return (
    <>
      <CelsiusInput value={celsius} onChange={setCelsius} />
      <FahrenheitDisplay celsius={celsius} />
    </>
  );
}

function CelsiusInput({ value, onChange }: { value: number; onChange: (n: number) => void }) {
  return <input type="number" value={value} onChange={(e) => onChange(Number(e.target.value))} />;
}

function FahrenheitDisplay({ celsius }: { celsius: number }) {
  return <p>{((celsius * 9) / 5 + 32).toFixed(1)} °F</p>;
}""",
        "language": "typescript",
        "key_points": [
            "Shared sibling state lives in common parent",
            "Pass value down, callbacks up",
            "Avoid duplicating derived state — compute instead",
            "Context/state libs when drilling gets deep",
        ],
    },
    "react-children-composition": {
        "explanation": (
            "The **`children`** prop (and explicit render props) enable **composition** over inheritance. "
            "Wrapper components like **Card**, **Modal**, or **Layout** accept arbitrary JSX without knowing "
            "inner content. **Compound components** (Tabs + TabList + TabPanel) share implicit state via Context. "
            "This pattern powers design systems and keeps components flexible."
        ),
        "code": """function Card({ title, children, footer }: {
  title: string;
  children: React.ReactNode;
  footer?: React.ReactNode;
}) {
  return (
    <article className="card">
      <header><h2>{title}</h2></header>
      <section>{children}</section>
      {footer && <footer>{footer}</footer>}
    </article>
  );
}

function App() {
  return (
    <Card title="Order #42" footer={<button>Print</button>}>
      <p>3 items — $149.99</p>
    </Card>
  );
}""",
        "language": "typescript",
        "key_points": [
            "children prop accepts any renderable React node",
            "Composition beats class inheritance",
            "Named slots via multiple props or compound components",
            "Render props: children as function for flexibility",
        ],
    },
    "react-fragments": {
        "explanation": (
            "Components must return **one root element**. **Fragments** (`<></>` or `<Fragment>`) group multiple "
            "children **without adding extra DOM nodes** — avoiding invalid HTML like `<div>` inside `<tr>`. "
            "Use **`<Fragment key={id}>`** when mapping lists that need keys on the grouped siblings."
        ),
        "code": """function TableRow({ name, email }: { name: string; email: string }) {
  return (
    <>
      <td>{name}</td>
      <td>{email}</td>
    </>
  );
}

function Glossary({ items }: { items: { term: string; def: string }[] }) {
  return (
    <dl>
      {items.map(({ term, def }) => (
        <Fragment key={term}>
          <dt>{term}</dt>
          <dd>{def}</dd>
        </Fragment>
      ))}
    </dl>
  );
}""",
        "language": "typescript",
        "key_points": [
            "No extra DOM wrapper node",
            "Short syntax <> cannot take key or attributes",
            "Fragment key={} required in keyed lists",
            "Fixes invalid nesting (table, dl structures)",
        ],
    },
    "react-styling": {
        "explanation": (
            "React supports **plain CSS** (global or imported), **CSS Modules** (scoped class names), "
            "**CSS-in-JS** (styled-components, Emotion), and **utility frameworks** (Tailwind). "
            "Apply styles via **`className`** (not `class`) or **`style={{ camelCase: 'value' }}`** for inline. "
            "Choose based on team conventions, SSR needs, and bundle size — no single winner."
        ),
        "code": """// CSS Module (styles.module.css: .button { ... })
import styles from './Button.module.css';

function Button({ primary, children }: { primary?: boolean; children: React.ReactNode }) {
  return (
    <button
      className={primary ? `${styles.button} ${styles.primary}` : styles.button}
      style={{ marginTop: '0.5rem' }}  // inline for dynamic one-offs
    >
      {children}
    </button>
  );
}

// Tailwind: <button className="rounded bg-blue-600 px-4 py-2 text-white">""",
        "language": "typescript",
        "key_points": [
            "className replaces HTML class attribute",
            "CSS Modules give local scope without runtime cost",
            "CSS-in-JS colocates styles; watch SSR and bundle size",
            "Tailwind popular for rapid consistent UI",
        ],
    },
    "react-strict-mode": {
        "explanation": (
            "**`<StrictMode>`** wraps your app in **development only** to surface problems: **double-invoking** "
            "effects and certain lifecycles to detect **missing cleanup**, warning about **deprecated APIs** "
            "(legacy context, findDOMNode), and identifying **unsafe patterns**. It does **not** render twice in "
            "production. Expect double fetch in dev — design idempotent effects."
        ),
        "code": """import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>
);

// Effect runs twice in dev — cleanup must handle it:
useEffect(() => {
  const sub = eventBus.subscribe(handleEvent);
  return () => sub.unsubscribe();
}, []);""",
        "language": "typescript",
        "key_points": [
            "Development-only — no production behavior change",
            "Double-invokes effects to find missing cleanup",
            "Warns on legacy/unsafe APIs",
            "Design effects to be idempotent",
        ],
    },
    "react-element-rendering": {
        "explanation": (
            "Every JSX tag becomes a **`React.createElement(type, props, ...children)`** call producing a "
            "**plain object** (React element) describing what to render — not a DOM node. React elements are "
            "**immutable**; new renders create new element objects. **Components** are functions/classes; "
            "**elements** are instructions to render them."
        ),
        "code": """import { createElement } from 'react';

// These are equivalent:
const jsx = <Greeting name="Ada" />;
const manual = createElement(Greeting, { name: 'Ada' });

// React element shape (simplified):
// { type: Greeting, props: { name: 'Ada' }, key: null, ref: null }

function Greeting({ name }: { name: string }) {
  return createElement('h1', null, `Hello, ${name}`);
}""",
        "language": "typescript",
        "key_points": [
            "JSX → createElement → plain object (element)",
            "Elements describe UI; React renders them to DOM",
            "Elements are cheap and immutable",
            "Component type can be string (intrinsic) or function/class",
        ],
    },
    "react-one-way-data-flow": {
        "explanation": (
            "React enforces **unidirectional data flow**: **props** travel **down** the tree; **events** travel **up** "
            "via callback props. This makes data changes **predictable and traceable** compared to two-way binding. "
            "Parent owns authoritative state; children request changes through **`onChange`** handlers. "
            "Global state (Context, Redux) still follows explicit dispatch/subscribe patterns."
        ),
        "code": """function App() {
  const [cart, setCart] = useState<CartItem[]>([]);

  const addToCart = (item: CartItem) => {
    setCart((prev) => [...prev, item]);  // parent owns state
  };

  return (
    <div>
      <ProductList onAdd={addToCart} />   {/* callback up */}
      <CartSummary items={cart} />         {/* data down */}
    </div>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Data down via props, events up via callbacks",
            "Single owner for each piece of state",
            "Predictable debugging vs mutable shared objects",
            "Redux/Context still explicit about updates",
        ],
    },
    "react-usecontext": {
        "explanation": (
            "**`useContext(MyContext)`** reads the nearest **`Provider`** value above in the tree. "
            "Use for **low-frequency global data**: theme, locale, auth user, feature flags. "
            "When the Provider **value changes**, all consuming components **re-render**. "
            "**Split contexts** by concern and **memoize the value object** to limit unnecessary renders."
        ),
        "code": """const ThemeContext = createContext<'light' | 'dark'>('light');

function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<'light' | 'dark'>('light');
  const value = useMemo(() => ({ theme, setTheme }), [theme]);

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

function ThemedButton() {
  const { theme, setTheme } = useContext(ThemeContext);
  return (
    <button className={theme} onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
      Toggle theme
    </button>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Avoid prop drilling for widely shared read-mostly data",
            "Memoize Provider value to prevent mass re-renders",
            "Split contexts — don't put everything in one",
            "Not a replacement for server cache (use React Query)",
        ],
    },
    "react-usereducer": {
        "explanation": (
            "**`useReducer(reducer, initialState)`** returns `[state, dispatch]` — ideal when **next state depends on "
            "previous** with **complex transitions** or multiple fields updated together. Pattern mirrors Redux: "
            "**action types**, **pure reducer**, predictable updates. Prefer over multiple **`useState`** hooks when "
            "logic grows — forms with many fields, wizards, or state machines."
        ),
        "code": """type State = { count: number; step: number };
type Action = { type: 'increment' } | { type: 'setStep'; step: number };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { ...state, count: state.count + state.step };
    case 'setStep':
      return { ...state, step: action.step };
    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0, step: 1 });
  return (
    <>
      <p>{state.count}</p>
      <button onClick={() => dispatch({ type: 'increment' })}>+{state.step}</button>
    </>
  );
}""",
        "language": "typescript",
        "key_points": [
            "dispatch({ type, payload }) — predictable updates",
            "Reducer must be pure — no side effects inside",
            "Good for complex form/wizard/state machine logic",
            "useReducer + Context can replace lightweight Redux",
        ],
    },
    "react-useref": {
        "explanation": (
            "**`useRef(initial)`** returns a **mutable `.current` box** that **persists across renders** without "
            "causing re-renders when updated. Common uses: **DOM references** (`inputRef.current.focus()`), "
            "**storing previous values**, **timer IDs**, and **avoiding stale closures** in callbacks. "
            "Do not read/write **`ref.current` during render** for UI logic — use state instead."
        ),
        "code": """function AutoFocusInput() {
  const inputRef = useRef<HTMLInputElement>(null);
  const renderCount = useRef(0);

  renderCount.current += 1;  // mutate without re-render

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  return <input ref={inputRef} placeholder="Focused on mount" />;
}

function usePrevious<T>(value: T) {
  const ref = useRef<T>();
  useEffect(() => { ref.current = value; }, [value]);
  return ref.current;
}""",
        "language": "typescript",
        "key_points": [
            "Updating ref.current does not trigger re-render",
            "Primary pattern for DOM imperatives (focus, scroll)",
            "Custom usePrevious built on useRef",
            "callback refs alternative for dynamic ref attachment",
        ],
    },
    "react-usememo": {
        "explanation": (
            "**`useMemo(() => compute(), [deps])`** caches a **computed value** between renders when dependencies "
            "are unchanged. Use for **expensive calculations** (filtering large lists, chart data) — not for every "
            "variable. **Premature memoization** adds complexity without benefit. Profile first. "
            "Distinct from **`React.memo`** which memoizes entire components."
        ),
        "code": """function ProductGrid({ products, filter }: {
  products: Product[];
  filter: string;
}) {
  const filtered = useMemo(
    () => products.filter((p) => p.name.toLowerCase().includes(filter.toLowerCase())),
    [products, filter]
  );

  const stats = useMemo(() => ({
    count: filtered.length,
    total: filtered.reduce((sum, p) => sum + p.price, 0),
  }), [filtered]);

  return (
    <>
      <p>{stats.count} items — ${stats.total.toFixed(2)}</p>
      {filtered.map((p) => <ProductCard key={p.id} product={p} />)}
    </>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Caches values — not functions (use useCallback for those)",
            "Only worth it for measurably expensive work",
            "Wrong deps → stale cached results",
            "React Compiler may auto-memoize in future",
        ],
    },
    "react-usecallback": {
        "explanation": (
            "**`useCallback(fn, deps)`** returns a **stable function reference** when deps unchanged. "
            "Critical when passing callbacks to **`React.memo`** children or **useEffect dependencies** — "
            "without it, inline functions recreate every render, breaking memoization. "
            "Do not wrap every handler — only when **referential equality** matters downstream."
        ),
        "code": """const MemoRow = React.memo(function Row({
  item,
  onDelete,
}: {
  item: Item;
  onDelete: (id: string) => void;
}) {
  return (
    <li>
      {item.name}
      <button onClick={() => onDelete(item.id)}>Delete</button>
    </li>
  );
});

function List({ items }: { items: Item[] }) {
  const [list, setList] = useState(items);

  const handleDelete = useCallback((id: string) => {
    setList((prev) => prev.filter((i) => i.id !== id));
  }, []);

  return (
    <ul>{list.map((item) => <MemoRow key={item.id} item={item} onDelete={handleDelete} />)}</ul>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Stable reference for memoized children and effect deps",
            "Not a performance fix by itself — pair with React.memo",
            "Inline handlers fine for non-memoized children",
            "useCallback(fn, deps) ≡ useMemo(() => fn, deps)",
        ],
    },
    "react-custom-hooks": {
        "explanation": (
            "**Custom hooks** extract reusable **stateful logic** into functions named **`useSomething`**. "
            "They compose built-in hooks and can return anything — state, refs, callbacks. "
            "Test with **`@testing-library/react`'s `renderHook`**. Rules of Hooks apply: only call from "
            "React functions, top level only. Examples: **`useDebounce`**, **`useLocalStorage`**, **`useFetch`**."
        ),
        "code": """function useDebounce<T>(value: T, delayMs: number): T {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const id = setTimeout(() => setDebounced(value), delayMs);
    return () => clearTimeout(id);
  }, [value, delayMs]);

  return debounced;
}

function Search() {
  const [query, setQuery] = useState('');
  const debouncedQuery = useDebounce(query, 300);

  useEffect(() => {
    if (debouncedQuery) searchApi(debouncedQuery);
  }, [debouncedQuery]);

  return <input value={query} onChange={(e) => setQuery(e.target.value)} />;
}""",
        "language": "typescript",
        "key_points": [
            "Prefix with use — convention and lint rule",
            "Share logic, not state — each call gets own state",
            "Compose hooks freely inside custom hooks",
            "Test with renderHook + act",
        ],
    },
    "react-useeffect-advanced": {
        "explanation": (
            "Common pitfalls: **missing dependencies** (eslint-plugin-react-hooks catches most), **stale closures** "
            "(capture old state — use functional updates or refs), **race conditions** (abort fetch on cleanup), "
            "and **fetch-in-effect** anti-pattern (prefer React Query). **Never disable the exhaustive-deps rule** "
            "without understanding the consequence."
        ),
        "code": """function LivePrice({ symbol }: { symbol: string }) {
  const [price, setPrice] = useState<number | null>(null);

  useEffect(() => {
    let cancelled = false;
    const ws = new WebSocket(`wss://api.example.com/prices/${symbol}`);

    ws.onmessage = (e) => {
      if (!cancelled) setPrice(JSON.parse(e.data).price);
    };

    return () => {
      cancelled = true;
      ws.close();
    };
  }, [symbol]);  // re-subscribe when symbol changes

  return <span>{price ?? '—'}</span>;
}""",
        "language": "typescript",
        "key_points": [
            "Include all values from component scope used in effect",
            "Cleanup prevents leaks and race conditions",
            "Functional setState avoids stale closure in timers",
            "React Query replaces most data-fetch useEffects",
        ],
    },
    "react-router": {
        "explanation": (
            "**React Router v6+** uses **declarative `<Routes>`** with **`element={<Component />}`** (not component prop). "
            "**Nested routes** render child routes in parent via **`<Outlet />`**. **`<Link>`** and **`useNavigate`** "
            "handle SPA navigation without full page reload. **URL params**: **`useParams()`**; **query strings**: "
            "**`useSearchParams()`**."
        ),
        "code": """import { BrowserRouter, Routes, Route, Link, Outlet, useParams } from 'react-router-dom';

function Layout() {
  return (
    <nav>
      <Link to="/">Home</Link>
      <Link to="/orders">Orders</Link>
      <Outlet />
    </nav>
  );
}

function OrderDetail() {
  const { orderId } = useParams();
  return <h1>Order {orderId}</h1>;
}

export function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="orders/:orderId" element={<OrderDetail />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}""",
        "language": "typescript",
        "key_points": [
            "element prop — not legacy component/render props",
            "Outlet renders nested child routes",
            "useParams, useSearchParams, useNavigate hooks",
            "BrowserRouter vs HashRouter for deployment context",
        ],
    },
    "react-router-data": {
        "explanation": (
            "React Router **data APIs** (v6.4+) add **`loader`**, **`action`**, and **`errorElement`** to routes. "
            "**Loaders** fetch data **before** the route renders — eliminating fetch-on-mount waterfalls. "
            "**Actions** handle form POST mutations. **`defer()`** streams slow data with Suspense. "
            "**Protected routes**: check auth in loader and **`redirect('/login')`**."
        ),
        "code": """import { createBrowserRouter, redirect, useLoaderData } from 'react-router-dom';

const router = createBrowserRouter([
  {
    path: '/dashboard',
    loader: async () => {
      const user = await getSession();
      if (!user) throw redirect('/login');
      return { stats: await fetchStats(user.id) };
    },
    element: <Dashboard />,
    errorElement: <RouteError />,
  },
]);

function Dashboard() {
  const { stats } = useLoaderData() as { stats: Stats };
  return <StatsPanel data={stats} />;
}""",
        "language": "typescript",
        "key_points": [
            "Loaders run before render — no useEffect fetch",
            "redirect() in loader for auth guards",
            "Actions for form mutations with revalidation",
            "Pairs naturally with Suspense via defer()",
        ],
    },
    "react-redux-toolkit": {
        "explanation": (
            "**Redux Toolkit (RTK)** is the official Redux approach: **`createSlice`** auto-generates actions and reducers, "
            "**`configureStore`** sets up DevTools and middleware, **`createAsyncThunk`** handles async flows. "
            "**RTK Query** adds data fetching/caching like React Query but integrated with Redux store. "
            "Use **`useSelector`** and **`useDispatch`** (or typed hooks) in components."
        ),
        "code": """import { createSlice, configureStore } from '@reduxjs/toolkit';
import { Provider, useSelector, useDispatch } from 'react-redux';

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [] as string[] },
  reducers: {
    addItem: (state, action) => { state.items.push(action.payload); },
    clear: (state) => { state.items = []; },
  },
});

const store = configureStore({ reducer: { cart: cartSlice.reducer } });

function CartBadge() {
  const count = useSelector((s: RootState) => s.cart.items.length);
  const dispatch = useDispatch();
  return <button onClick={() => dispatch(cartSlice.actions.clear())}>{count} items</button>;
}""",
        "language": "typescript",
        "key_points": [
            "createSlice reduces boilerplate vs hand-written Redux",
            "Immer built-in — \"mutate\" draft state safely",
            "RTK Query for API cache in Redux apps",
            "Use for large apps with complex shared client state",
        ],
    },
    "react-zustand": {
        "explanation": (
            "**Zustand** is a minimal **hook-based store** — `create((set) => ({ ... }))` with no Provider required "
            "(unless SSR). Components subscribe to **slices** via selectors: **`useStore(s => s.count)`** — "
            "only re-render when selected slice changes. Far less boilerplate than Redux for **medium complexity** "
            "client state. Combine with React Query for server state."
        ),
        "code": """import { create } from 'zustand';

type UIStore = {
  sidebarOpen: boolean;
  toggleSidebar: () => void;
};

const useUIStore = create<UIStore>((set) => ({
  sidebarOpen: false,
  toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
}));

function SidebarToggle() {
  const open = useUIStore((s) => s.sidebarOpen);
  const toggle = useUIStore((s) => s.toggleSidebar);
  return <button onClick={toggle}>{open ? 'Close' : 'Open'} sidebar</button>;
}""",
        "language": "typescript",
        "key_points": [
            "No Provider wrapper needed (client-side)",
            "Selector subscriptions minimize re-renders",
            "Great middle ground vs Context or Redux",
            "Persist middleware for localStorage sync",
        ],
    },
    "react-tanstack-query": {
        "explanation": (
            "**TanStack Query** manages **server/async state** — caching, background refetch, stale-while-revalidate, "
            "deduplication, pagination, and optimistic updates. **`useQuery`** for reads, **`useMutation`** for writes. "
            "Replaces most **`useEffect + useState` fetch** patterns. Configure **`staleTime`**, **`gcTime`**, and "
            "**query keys** for predictable cache behavior."
        ),
        "code": """import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function OrdersList() {
  const queryClient = useQueryClient();

  const { data, isLoading, error } = useQuery({
    queryKey: ['orders'],
    queryFn: () => fetch('/api/orders').then((r) => r.json()),
    staleTime: 60_000,
  });

  const cancel = useMutation({
    mutationFn: (id: string) => fetch(`/api/orders/${id}`, { method: 'DELETE' }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['orders'] }),
  });

  if (isLoading) return <Spinner />;
  if (error) return <ErrorState />;
  return data.map((o: Order) => (
    <OrderRow key={o.id} order={o} onCancel={() => cancel.mutate(o.id)} />
  ));
}""",
        "language": "typescript",
        "key_points": [
            "Server state ≠ client state — don't put API cache in Redux",
            "queryKey drives cache identity and invalidation",
            "Automatic background refetch on focus/reconnect",
            "DevTools visualize cache and query lifecycle",
        ],
    },
    "react-error-boundaries": {
        "explanation": (
            "**Error boundaries** catch **JavaScript errors during rendering**, lifecycle methods, and child tree "
            "construction. They display fallback UI via **`getDerivedStateFromError`** / **`componentDidCatch`** "
            "(class) or libraries like **react-error-boundary**. They **do NOT** catch: event handler errors, "
            "async errors, SSR errors, or errors in the boundary itself."
        ),
        "code": """import { Component, ErrorInfo, ReactNode } from 'react';

type Props = { children: ReactNode; fallback: ReactNode };
type State = { hasError: boolean };

class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError(): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    logToService(error, info.componentStack);
  }

  render() {
    return this.state.hasError ? this.props.fallback : this.props.children;
  }
}

// Usage: wrap route segments or risky widgets
// <ErrorBoundary fallback={<p>Something broke</p>}><Dashboard /></ErrorBoundary>""",
        "language": "typescript",
        "key_points": [
            "Only class components natively — or use a library wrapper",
            "Catches render errors — not onClick/async errors",
            "Granular boundaries per route/feature — not one global",
            "Log to Sentry/App Insights in componentDidCatch",
        ],
    },
    "react-portals": {
        "explanation": (
            "**`createPortal(child, domNode)`** renders children into a **DOM node outside the parent hierarchy** "
            "while keeping them in the **same React tree** (events bubble through React, not DOM). "
            "Essential for **modals, tooltips, dropdowns** that must escape `overflow: hidden` or z-index stacking. "
            "Mount portal target (e.g., `#modal-root`) in `index.html`."
        ),
        "code": """import { createPortal } from 'react-dom';

function Modal({ open, onClose, children }: {
  open: boolean;
  onClose: () => void;
  children: React.ReactNode;
}) {
  if (!open) return null;

  return createPortal(
    <div className="overlay" onClick={onClose}>
      <div className="dialog" onClick={(e) => e.stopPropagation()}>
        {children}
      </div>
    </div>,
    document.getElementById('modal-root')!
  );
}""",
        "language": "typescript",
        "key_points": [
            "DOM elsewhere — React tree unchanged",
            "Events still bubble in React tree order",
            "Standard pattern for modals and popovers",
            "Accessibility: focus trap + aria-modal on dialog",
        ],
    },
    "react-forwardref": {
        "explanation": (
            "Function components don't expose **`ref`** by default. **`forwardRef`** forwards the parent's ref to "
            "a DOM node or **`useImperativeHandle`** custom API. Common in **design system inputs/buttons** where "
            "consumers need **`focus()`**, **`scrollIntoView()`**, or integration with third-party libraries."
        ),
        "code": """import { forwardRef, useImperativeHandle, useRef } from 'react';

export const TextInput = forwardRef<HTMLInputElement, { label: string }>(
  function TextInput({ label }, ref) {
    return (
      <label>
        {label}
        <input ref={ref} type="text" className="input" />
      </label>
    );
  }
);

// React 19+: ref can be a regular prop — forwardRef optional
function Form() {
  const inputRef = useRef<HTMLInputElement>(null);
  return <TextInput ref={inputRef} label="Email" />;
}""",
        "language": "typescript",
        "key_points": [
            "forwardRef passes ref to inner DOM or imperative handle",
            "useImperativeHandle exposes limited parent API",
            "React 19 treats ref as prop on function components",
            "Prefer declarative props over imperative refs when possible",
        ],
    },
    "react-memo-optimization": {
        "explanation": (
            "**`React.memo(Component)`** skips re-render if **props are shallow-equal** to previous. "
            "Useful for **expensive pure components** in large lists or charts. **Worthless** if props are "
            "new objects/functions every parent render — pair with **useMemo/useCallback**. "
            "**Always profile** with React DevTools Profiler before memoizing everything."
        ),
        "code": """const ExpensiveChart = React.memo(function ExpensiveChart({
  data,
  onPointClick,
}: {
  data: DataPoint[];
  onPointClick: (id: string) => void;
}) {
  // heavy D3/canvas rendering...
  return <canvas /* ... */ />;
});

function Dashboard({ rawData }: { rawData: DataPoint[] }) {
  const chartData = useMemo(() => transform(rawData), [rawData]);
  const handleClick = useCallback((id: string) => analytics.track(id), []);

  return <ExpensiveChart data={chartData} onPointClick={handleClick} />;
}""",
        "language": "typescript",
        "key_points": [
            "Shallow compare props — default comparator",
            "Combine with stable props from useMemo/useCallback",
            "Don't memo every component — measure first",
            "custom compare function for deep/partial props",
        ],
    },
    "react-form-validation": {
        "explanation": (
            "Production forms combine **controlled inputs** with **schema validation** (**Zod**, **Yup**) and "
            "either manual state or **React Hook Form (RHF)** for performance. RHF uses **refs** internally to "
            "minimize re-renders. Display errors on **`onBlur`** or submit; use **`aria-invalid`** and "
            "**`aria-describedby`** for accessibility."
        ),
        "code": """import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';

const schema = z.object({
  email: z.string().email('Invalid email'),
  age: z.coerce.number().min(18, 'Must be 18+'),
});

type FormData = z.infer<typeof schema>;

function SignupForm() {
  const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
    resolver: zodResolver(schema),
  });

  return (
    <form onSubmit={handleSubmit((data) => api.signup(data))}>
      <input {...register('email')} aria-invalid={!!errors.email} />
      {errors.email && <span role="alert">{errors.email.message}</span>}
      <button type="submit">Sign up</button>
    </form>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Schema validation (Zod) at boundary — type-safe",
            "React Hook Form minimizes re-renders vs all-controlled",
            "Validate on blur/submit — not every keystroke for UX",
            "Wire a11y: aria-invalid, role=alert for errors",
        ],
    },
    "react-testing-rtl": {
        "explanation": (
            "**React Testing Library (RTL)** encourages testing **user-visible behavior**, not implementation "
            "details. Query by **role, label, text** — `getByRole('button', { name: /submit/i })`. "
            "Use **`userEvent`** over **`fireEvent`** for realistic interactions. "
            "**Avoid** testing internal state or shallow rendering — refactor if tests are brittle."
        ),
        "code": """import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Counter } from './Counter';

test('increments count on click', async () => {
  const user = userEvent.setup();
  render(<Counter initial={0} />);

  const button = screen.getByRole('button', { name: /count: 0/i });
  await user.click(button);

  expect(screen.getByRole('button', { name: /count: 1/i })).toBeInTheDocument();
});

// Prefer queries: getByRole > getByLabelText > getByText > getByTestId""",
        "language": "typescript",
        "key_points": [
            "Test what users see and do — not component internals",
            "getByRole is the most accessible query priority",
            "userEvent simulates real pointer/keyboard events",
            "Mock network at MSW layer — not fetch globally",
        ],
    },
    "react-typescript": {
        "explanation": (
            "Type **props** with **`interface` or `type`**, **`children: React.ReactNode`**, and optional **`?`**. "
            "Events: **`React.ChangeEvent<HTMLInputElement>`**, **`React.FormEvent`**. "
            "Generic components: **`function List<T>({ items }: { items: T[] })`**. "
            "Use **`ComponentPropsWithoutRef<'button'>`** to extend native elements. Prefer explicit props over **`React.FC`** "
            "(implicit children removed in modern TS)."
        ),
        "code": """type ButtonProps = React.ComponentPropsWithoutRef<'button'> & {
  variant?: 'primary' | 'secondary';
};

function Button({ variant = 'primary', children, ...rest }: ButtonProps) {
  return <button className={`btn-${variant}`} {...rest}>{children}</button>;
}

type ApiState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; error: Error };""",
        "language": "typescript",
        "key_points": [
            "Explicit props typing — avoid React.FC for new code",
            "Discriminated unions for async/UI state machines",
            "ComponentPropsWithoutRef extends native elements",
            "Strict null checks catch undefined render bugs",
        ],
    },
    "react-context-patterns": {
        "explanation": (
            "A **single giant Context** with `{ user, theme, cart, ... }` causes **every consumer to re-render** "
            "when any field changes. **Split by update frequency**, **memoize value** with useMemo, or use "
            "**use-context-selector** / state libraries. Pass **dispatch-only context** separate from **state context** "
            "so components that only dispatch don't re-render on state changes."
        ),
        "code": """const CartStateContext = createContext<CartItem[]>([]);
const CartDispatchContext = createContext<React.Dispatch<CartAction>>(() => {});

function CartProvider({ children }: { children: React.ReactNode }) {
  const [items, dispatch] = useReducer(cartReducer, []);

  return (
    <CartDispatchContext.Provider value={dispatch}>
      <CartStateContext.Provider value={items}>{children}</CartStateContext.Provider>
    </CartDispatchContext.Provider>
  );
}

// Components that only add items subscribe to dispatch — never re-render on item changes
function AddToCartButton({ productId }: { productId: string }) {
  const dispatch = useContext(CartDispatchContext);
  return <button onClick={() => dispatch({ type: 'ADD', productId })}>Add</button>;
}""",
        "language": "typescript",
        "key_points": [
            "Split state vs dispatch contexts",
            "Memoize Provider value objects",
            "Context for low-update-frequency data",
            "Zustand selectors scale better for frequent updates",
        ],
    },
    "react-suspense-data": {
        "explanation": (
            "**Suspense** shows **`fallback`** while child components **suspend** (throw a promise during render). "
            "React Query **`useSuspenseQuery`**, Relay, and Next.js streaming use this pattern. "
            "Eliminates **`isLoading`** boilerplate — boundaries declare loading UI declaratively. "
            "**Error boundaries** pair with Suspense for error states."
        ),
        "code": """import { Suspense } from 'react';
import { useSuspenseQuery } from '@tanstack/react-query';

function OrderDetails({ id }: { id: string }) {
  const { data } = useSuspenseQuery({
    queryKey: ['order', id],
    queryFn: () => fetchOrder(id),
  });
  return <OrderView order={data} />;
}

function OrderPage({ id }: { id: string }) {
  return (
    <ErrorBoundary fallback={<ErrorPage />}>
      <Suspense fallback={<OrderSkeleton />}>
        <OrderDetails id={id} />
      </Suspense>
    </ErrorBoundary>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Child throws promise → nearest Suspense shows fallback",
            "useSuspenseQuery removes manual loading flags",
            "Nest Suspense for progressive loading (shell + content)",
            "Combine with ErrorBoundary for complete async UX",
        ],
    },
    "react-lazy-code-splitting": {
        "explanation": (
            "**`React.lazy(() => import('./Heavy'))`** code-splits at the **route or feature** level — "
            "the chunk loads only when rendered. Must wrap in **`<Suspense fallback={...}>`**. "
            "Next.js **`dynamic()`** adds SSR options. Split on **routes and heavy modals**, not every component."
        ),
        "code": """import { lazy, Suspense } from 'react';

const AdminDashboard = lazy(() => import('./AdminDashboard'));
const ChartPanel = lazy(() => import('./ChartPanel'));

function App() {
  return (
    <Routes>
      <Route
        path="/admin"
        element={
          <Suspense fallback={<PageLoader />}>
            <AdminDashboard />
          </Suspense>
        }
      />
    </Routes>
  );
}

// Vite/Webpack create separate chunks automatically from dynamic import()""",
        "language": "typescript",
        "key_points": [
            "lazy + import() = automatic code splitting",
            "Suspense required — shows fallback while chunk loads",
            "Split by route/feature — biggest bundle wins",
            "Preload on hover/focus for perceived speed",
        ],
    },
    "react-performance": {
        "explanation": (
            "Measure with **React DevTools Profiler** and **Web Vitals** first. Techniques: **code splitting**, "
            "**virtualization** (react-window) for long lists, **memoization** where profiling shows waste, "
            "**debounce** expensive search, **Web Workers** for heavy compute, **avoid anonymous objects in deps**. "
            "React 18 **automatic batching** and **transitions** keep UI responsive during heavy updates."
        ),
        "code": """import { useTransition, useDeferredValue } from 'react';
import { FixedSizeList as List } from 'react-window';

function SearchResults({ query, items }: { query: string; items: Item[] }) {
  const [isPending, startTransition] = useTransition();
  const [filter, setFilter] = useState('');
  const deferredFilter = useDeferredValue(filter);

  const handleChange = (value: string) => {
    setFilter(value);  // urgent — input stays responsive
    startTransition(() => setFilter(value));  // non-urgent filter can lag
  };

  const filtered = useMemo(
    () => items.filter((i) => i.name.includes(deferredFilter)),
    [items, deferredFilter]
  );

  return (
    <>
      <input value={filter} onChange={(e) => handleChange(e.target.value)} />
      {isPending && <Spinner />}
      <List height={400} itemCount={filtered.length} itemSize={48} width="100%"
        itemData={filtered}>{Row}</List>
    </>
  );
}""",
        "language": "typescript",
        "key_points": [
            "Profile before optimizing — avoid cargo-cult memo",
            "Virtualize lists with 100+ DOM-heavy rows",
            "useTransition marks non-urgent state updates",
            "useDeferredValue defers expensive derived renders",
        ],
    },
    "react-use-transition": {
        "explanation": (
            "**`useTransition`** returns **`[isPending, startTransition]`**. Wrap state updates that cause "
            "**slow re-renders** (filtering huge lists, tab switches) in **`startTransition`** — React treats them "
            "as **non-urgent** and keeps the UI responsive. **`isPending`** drives loading indicators. "
            "Part of **Concurrent React** — updates can be interrupted."
        ),
        "code": """function TabbedPanel({ tabs }: { tabs: Tab[] }) {
  const [activeTab, setActiveTab] = useState(tabs[0].id);
  const [isPending, startTransition] = useTransition();

  const selectTab = (id: string) => {
    startTransition(() => {
      setActiveTab(id);  // heavy panel render won't block input
    });
  };

  return (
    <>
      <TabBar tabs={tabs} active={activeTab} onSelect={selectTab} disabled={isPending} />
      {isPending ? <TabSkeleton /> : <TabContent id={activeTab} />}
    </>
  );
}""",
        "language": "typescript",
        "key_points": [
            "startTransition wraps setState for low-priority updates",
            "isPending true while transition render in progress",
            "Keeps typing/clicks responsive during heavy renders",
            "Different from debounce — still renders all states",
        ],
    },
    "react-ssr-nextjs": {
        "explanation": (
            "**CSR** — client fetches and renders (SPA). **SSR** — server renders HTML per request (SEO, TTFB). "
            "**SSG** — HTML at build time (blogs, marketing). **ISR** — SSG + periodic revalidation. "
            "**Next.js App Router** defaults to Server Components; **`'use client'`** marks interactive boundaries. "
            "Choose SSR/SSG for SEO-critical pages; CSR for authenticated dashboards."
        ),
        "code": """// app/products/[id]/page.tsx — Server Component (default)
export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await db.product.findUnique({ where: { id: params.id } });
  return (
    <main>
      <h1>{product.name}</h1>
      <AddToCartButton productId={product.id} />  {/* client component */}
    </main>
  );
}

// Static generation with revalidation (ISR)
export const revalidate = 3600;  // regenerate every hour""",
        "language": "typescript",
        "key_points": [
            "SSR = request-time HTML; SSG = build-time HTML",
            "ISR balances static speed with fresh data",
            "App Router: Server Components by default",
            "'use client' for hooks, events, browser APIs",
        ],
    },
    "react-server-components": {
        "explanation": (
            "**React Server Components (RSC)** run **only on the server** — zero JavaScript sent to client for that "
            "component. They can **async/await** database calls directly, access secrets, and **stream** HTML. "
            "**Client Components** (`'use client'`) handle interactivity. **Serialization boundary** — pass plain "
            "data/props, not functions, from Server to Client Components."
        ),
        "code": """// Server Component — no 'use client'
async function OrderList() {
  const orders = await sql`SELECT * FROM orders LIMIT 20`;  // direct DB
  return (
    <ul>
      {orders.map((o) => (
        <li key={o.id}>
          {o.id} — <CancelButton orderId={o.id} />  {/* Client child */}
        </li>
      ))}
    </ul>
  );
}

// Client Component — interactivity
'use client';
export function CancelButton({ orderId }: { orderId: string }) {
  return <button onClick={() => cancelOrder(orderId)}>Cancel</button>;
}""",
        "language": "typescript",
        "key_points": [
            "RSC = zero client bundle for server-only UI",
            "Async components — await data in render",
            "Cannot use hooks or browser APIs in RSC",
            "Props to Client Components must be serializable",
        ],
    },
    "react-18-concurrent": {
        "explanation": (
            "**React 18** introduced **Concurrent Rendering** — work can be **interrupted and prioritized**. "
            "**Automatic batching** merges setStates in timeouts/promises/fetches. **`createRoot`** replaces "
            "**`ReactDOM.render`**. **Streaming SSR** with **`renderToPipeableStream`** sends HTML progressively. "
            "**Suspense** on server enables shell-first loading."
        ),
        "code": """import { createRoot } from 'react-dom/client';
import { Suspense } from 'react';

// React 18 root API — enables concurrent features
createRoot(document.getElementById('root')!).render(
  <Suspense fallback={<AppShell />}>
    <App />
  </Suspense>
);

// Automatic batching — single re-render
async function save() {
  setSaving(true);
  await api.save();
  setSaving(false);   // batched with above in React 18
  setSaved(true);
}""",
        "language": "typescript",
        "key_points": [
            "createRoot required — legacy render is deprecated",
            "Automatic batching everywhere — fewer renders",
            "Concurrent mode enables transitions and Suspense SSR",
            "StrictMode double-invoke helps find effect bugs",
        ],
    },
    "react-19-features": {
        "explanation": (
            "**React 19** adds **Actions** — async functions in transitions with pending states via **`useTransition`** "
            "or **`useActionState`**. **`useOptimistic`** for instant UI during slow mutations. **`ref` as prop** "
            "eliminates forwardRef boilerplate. **Document metadata** (`<title>`, `<meta>`) in components. "
            "**Resource preloading** APIs for styles/fonts."
        ),
        "code": """'use client';
import { useActionState, useOptimistic } from 'react';

async function addComment(prev: Comment[], formData: FormData) {
  const text = formData.get('text') as string;
  const comment = await api.postComment(text);
  return [...prev, comment];
}

function CommentThread({ initial }: { initial: Comment[] }) {
  const [comments, submitAction, isPending] = useActionState(addComment, initial);
  const [optimistic, addOptimistic] = useOptimistic(comments, (state, text: string) => [
    ...state,
    { id: 'temp', text, pending: true },
  ]);

  return (
    <form action={async (fd) => { addOptimistic(fd.get('text') as string); await submitAction(fd); }}>
      <input name="text" disabled={isPending} />
    </form>
  );
}""",
        "language": "typescript",
        "key_points": [
            "useActionState — form actions with pending/error state",
            "useOptimistic — instant feedback before server confirms",
            "ref as regular prop on function components",
            "Actions integrate forms + transitions + mutations",
        ],
    },
    "react-security-xss": {
        "explanation": (
            "React **escapes strings in JSX** by default — `{userInput}` renders as text, not HTML. "
            "**XSS risk** enters via **`dangerouslySetInnerHTML`**, rendering unsanitized HTML from APIs, "
            "**URL injection** (`javascript:` URLs), and **third-party scripts**. Sanitize with **DOMPurify** "
            "before dangerouslySetInnerHTML. **CSP headers** add defense in depth. Never store tokens in localStorage "
            "if XSS is a concern — prefer httpOnly cookies."
        ),
        "code": """import DOMPurify from 'dompurify';

function ArticleBody({ html }: { html: string }) {
  const clean = DOMPurify.sanitize(html, { USE_PROFILES: { html: true } });
  return <div dangerouslySetInnerHTML={{ __html: clean }} />;
}

// ✅ Safe — escaped automatically
function Comment({ text }: { text: string }) {
  return <p>{text}</p>;
}

// ❌ Never: <a href={userUrl}> — validate protocol !== 'javascript:'
function SafeLink({ href, children }: { href: string; children: React.ReactNode }) {
  const safe = href.startsWith('https://') ? href : '#';
  return <a href={safe} rel="noopener noreferrer">{children}</a>;
}""",
        "language": "typescript",
        "key_points": [
            "JSX auto-escapes — XSS mainly from raw HTML injection",
            "DOMPurify before dangerouslySetInnerHTML",
            "Validate URLs — block javascript: protocol",
            "CSP + httpOnly cookies reduce XSS blast radius",
        ],
    },
    "react-micro-frontends": {
        "explanation": (
            "**Micro-frontends** split a shell app into **independently deployable** frontend teams/modules. "
            "**Module Federation** (Webpack/Vite) shares React runtime and loads remote bundles at runtime. "
            "**single-spa** orchestrates multiple frameworks on one page. Challenges: **shared dependencies** "
            "(one React instance), **routing**, **consistent design tokens**, and **version drift**."
        ),
        "code": """// Shell app — dynamic remote (Module Federation concept)
import { lazy, Suspense } from 'react';

const RemoteOrders = lazy(() => import('ordersApp/OrdersPage'));

function Shell() {
  return (
    <Layout>
      <nav>...</nav>
      <Suspense fallback={<Loader />}>
        <RemoteOrders />  {/* team B deploys independently */}
      </Suspense>
    </Layout>
  );
}

// webpack.config — shared: { react: { singleton: true, requiredVersion: '^18' } }""",
        "language": "typescript",
        "key_points": [
            "Independent deploy per team/feature",
            "Module Federation shares deps at runtime",
            "Singleton React — avoid duplicate React copies",
            "Trade-off: operational complexity vs team autonomy",
        ],
    },
    "react-hydration": {
        "explanation": (
            "**Hydration** attaches React event listeners and reconciler to **server-rendered HTML**. "
            "**Hydration mismatch** occurs when client render output **differs from server HTML** — "
            "often from **`Date.now()`**, **`window`**, random IDs, or browser extensions. React 18 "
            "**recoverable errors** try to client-render the subtree. Fix: **render same on server/client**, "
            "use **`useEffect`** for client-only values, **`suppressHydrationWarning`** sparingly."
        ),
        "code": """// ❌ Mismatch — Date differs server vs client
// <span>{new Date().toLocaleString()}</span>

function ClientTime() {
  const [time, setTime] = useState<string | null>(null);

  useEffect(() => {
    setTime(new Date().toLocaleString());  // client-only after hydration
  }, []);

  return <span suppressHydrationWarning>{time ?? '—'}</span>;
}

// Next.js: dynamic(() => import('./Map'), { ssr: false }) for browser-only widgets""",
        "language": "typescript",
        "key_points": [
            "Server and client initial render must match",
            "useEffect for window/localStorage/Date access",
            "suppressHydrationWarning only for known benign diffs",
            "Check extensions and invalid HTML nesting too",
        ],
    },
    "react-compiler-optimization": {
        "explanation": (
            "The **React Compiler** (formerly \"React Forget\") analyzes components at **build time** and "
            "automatically inserts **memoization** — reducing need for manual **`useMemo`**, **`useCallback`**, "
            "and **`React.memo`**. It enforces **Rules of React** and skips unsafe patterns. "
            "Enable in **React 19+** projects; still understand manual optimization for interviews and legacy code."
        ),
        "code": """// Before compiler — manual memoization everywhere
const MemoList = React.memo(function List({ items, onSelect }: Props) {
  const sorted = useMemo(() => [...items].sort(), [items]);
  const handle = useCallback((id: string) => onSelect(id), [onSelect]);
  return sorted.map((i) => <Row key={i.id} item={i} onSelect={handle} />);
});

// With React Compiler — write idiomatic code, compiler memoizes safely
function List({ items, onSelect }: Props) {
  const sorted = [...items].sort();  // compiler may auto-memoize
  return sorted.map((i) => <Row key={i.id} item={i} onSelect={onSelect} />);
}

// babel-plugin-react-compiler in build pipeline""",
        "language": "typescript",
        "key_points": [
            "Compile-time auto-memoization — less manual hooks",
            "Still need architectural wins: split code, virtualize",
            "Compiler enforces Rules of Hooks/React",
            "Know manual patterns — most codebases aren't compiled yet",
        ],
    },
}
