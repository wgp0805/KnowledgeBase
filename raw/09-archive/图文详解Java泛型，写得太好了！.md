---
title: "图文详解Java泛型，写得太好了！"
source: "https://mp.weixin.qq.com/s/JcNCAfSOE60q8r0MmHikHw"
---
*2026年2月18日 09:14*

```
大家好，我是锋哥。
```

泛型—— 一种可以接收数据类型的数据类型，本文将通俗讲解Java泛型的优点、方法及相关细节。

## 一、泛型的引入

我们都知道，继承是面向对象的三大特性之一，比如在我们向集合中添加元素的过程中add()方法里填入的是Object类，而Object又是所有类的父类，这就产生了一个问题——添加的类型无法做到统一 由此就可能产生在遍历集合取出元素时类型不统一而报错问题。

例如：我向一个ArrayList集合中添加Person类的对象，但是不小心手贱添加了一个Boy类的对象，这就会导致如下结果

![图片](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/a99c4be3bd7c66c5817b872c6388667d_MD5.png)

传统的方式不能对加入到集合ArrayList中的数据类型进行约束(不安全)遍历的时候，需要进行类型转换,如果集合中的数据量较大，对效率有影响 这就极大地降低了程序的健壮性，因此设计者针对此问题引入了泛型！

## 二、使用泛型的好处

1.提升了程序的健壮性和规范性

针对上述问题，当我们采用泛型就会显得非常简单，只需要在编译类型后利用泛型指定一个特定类型，编译器就会自动检测出不符合规范的类并抛出错误提示

![图片](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/a251b3bd73362658ec5ed6a25ffb0308_MD5.png)

2.编译时,检查添加元素的类型，提高了安全性

3.减少了类型转换的次数,提高效率

- **当不使用泛型时：**
![图片](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/d3bb573d432d28f0ec0e0c904e2c6817_MD5.png)

- **当使用泛型时：**
![图片](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/ccba8933c8d96ef9ae20e0d554b8631f_MD5.png)

4.在类声明时通过一个标识可以表示属性类型、方法的返回值类型、参数类型

```java
class Person<E> {
    E s;   //可以是属性类型
    public Person(E s) {  //可以是参数类型
        this.s = s;
    }
    public E f() { //可以是返回类型
        return s;
    }
    public void show() {
        
            System.out.println(s.getClass());
            //显示S的运行类型
    }
}
```

可以这样理解：上述的class Person< E >中的“E”相当于这里的E是一个躯壳 占位用的 以后定义的时候程序员可以自己去自定义。

就像这样

```java
public static void main(String[] args) {
    Person<String> person1 = new Person<String>("xxxx");// E->String
    
            person.show();
          
    Person<Integer> person2 = new Person<Integer>(123); // E->Integer
    
            person.show();
          
}
运行结果：
class java.lang.String
class java.lang.Integer
```

## 三、泛型常见用法

### 1.定义泛型接口

曾经写接口的时候都没有定义泛型，它默认的就是Object类，其实这样写是不规范的！

如果说接口的存在是一种规范，那泛型接口就是规范中的规范

```java
interface Im<U,R>{
    void hi(R r);
    void hello(R r1,R r2,U u1,U u2);
    default R method(U u){
        return null;
    }
}
```

在上述的泛型接口中已经规定传入其中的必须是U，R类的对象，那么当我们传入其他类的对象时就会报错，如图：

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

根据规则，当我们实现接口时，就必须实现他的所有方法，而在这时我们就可以向<U,R>中传入我们自己规定的类。在IDEA中重写接口中的方法时，编译器会自动将<U,R>替换成我们事先规定的类。

### 2.定义泛型集合

1.使用泛型方式给HashSet中放入三个学生对象，并输出对象信息

```java
HashSet<Student> students = new HashSet<Student>();

           students.add(
         new Student("懒羊羊",21));

           students.add(
         new Student("喜羊羊",41));

           students.add(
         new Student("美羊羊",13));
for (Student student :students) {
    
           System.out.println(student);
         
}
```

上述的 泛型中Student的是我事先定义好的一个类，把它放到其中作为泛型来约束传入的对象，以及在遍历时减少转型的次数提高效率

2.使用泛型方式给HashMap中放入三个学生对象，并输出对象信息

```java
HashMap<String, Student> hm = new HashMap<String, Student>();
// K-> String  V->Student与下面的对应

            hm.put(
          "001",new Student("喜羊羊",21));

            hm.put(
          "002",new Student("懒羊羊",32));

            hm.put(
          "003",new Student("美羊羊",43));
Set<
            Map.Entry>
           ek=
            hm.entrySet();
          
Iterator<
            Map.Entry Student>> iterator = 
            ek.iterator();
          //取出迭代器
while (
            iterator.hasNext())
           {
    
            Map.Entry Student> next =  
            iterator.next();
          
    
            System.out.println(next.getKey()+
          " - "+
            next.getValue());
          
}
```

\[HashMap是一个双列集合，以K-V\]的方式存储对象，因此在使用泛型时要向其中传入两个类型

> 我们都知道使用迭代器遍历HashMap时要先通过 `entrySet()` 取出键值对，然后通过转型得到对应的类来得到对象信息。而在使用泛型定义 `[K-V]` 就规定了取出的键值对的类型，所以就省去了转型这一步骤，同样也使程序变得简单，高效。

## 四、泛型使用细节

### 1.<>中类型规范

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

### 2.继承性体现

在给泛型指定具体类型后，可以传入该类型或者其子类类型

```java
P<A> ap = new P<A>(new A());
P<A> ap1 = new P<A>(new B()); //A的子类
class A {}
class B extends A{}
```

### 3.简写形式

```
P<A> ap = new P(new A());
```

## 五、自定义泛型

### 1.自定义方法使用类声明的泛型

> 在形参列表中传入的数据类型与泛型不一致时会报错，体现规范性

```java
public static void main(String[] args) {
    U<String, Double, Integer> u = new U<>();
    
            u.hi(
          "hello", 1.0);  //X->String Y->Double
}
class U<X, Y, Z> {
    public void hi(X x, Y y) {} //使用类声明的泛型
}
```

### 2.自定义泛型方法

```java
public static void main(String[] args) {
    U<String, Double, Integer> u = new U<>();
    
            u.m1(
          "xx",22);
    //当调用方法时，传入参数编译器会自己确定类型 会自动装箱
}
class U<X, Y, Z> {
    public <X,Y> void m1(X x,Y y){} //自定义泛型方法
}
```

这里的自动装箱很有意思，他是在三个类型中自动匹配当前输入的数据类型，也不用考虑顺序问题，如图所示
[Open: file-20260520150720970.png](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/e003737b2df08cab33bbc952fef1d11b_MD5.jpg)
![](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/e003737b2df08cab33bbc952fef1d11b_MD5.jpg)
### 3.注意事项

①泛型数组不能初始化，因为数组在 new 不能确定A 的类型，就无法在内存开空间

错误写法: A\[\] a=new A\[\];

②静态方法不能使用类定义的泛型

[Open: file-20260520150731713.png](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/7d10af4d8e564bf57e8264fe33742f2a_MD5.jpg)
![](assets/%E5%9B%BE%E6%96%87%E8%AF%A6%E8%A7%A3Java%E6%B3%9B%E5%9E%8B%EF%BC%8C%E5%86%99%E5%BE%97%E5%A4%AA%E5%A5%BD%E4%BA%86%EF%BC%81/7d10af4d8e564bf57e8264fe33742f2a_MD5.jpg)

原因是静态成员是和类相关的,在类加载时,对象还没有创建所以，如果静态方法和静态属性使用了泛型，JVM就无法完成初始化。
