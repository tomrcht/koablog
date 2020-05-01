---
Title: Swift test
Date: 2020-04-01 19:56
Modified: 2020-04-01 20:00
Category: Swift
Tags: swift, interface builder, xcode
Slug: swift-test
Authors: Alexis Metaireau, Conan Doyle
Summary: Whatever works in Swift
Status: draft
---

Salut ca va ? Moi aussi

```Swift
final class Manager: SomeProtocol {
  public static let shared = Manager()

  public func protocolMethod(value: String) -> Void {
    "(" + value + ")" // implicit return
  }
}
```
